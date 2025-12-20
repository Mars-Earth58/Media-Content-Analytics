import csv
from collections import defaultdict
import statistics
import matplotlib.pyplot as plt

# File names
CSV_FILE = "tickets.csv"
CHART_FILE = "ticket_summary.png"
TECH_CHART_FILE = "technician_ticket_counts.png"

# SLA rules in hours
SLA_RULES = {
    "High": 4.0,
    "Medium": 8.0,
    "Low": 24.0,
}


def load_tickets(csv_file):
    tickets = []
    with open(csv_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not any(row.values()):
                continue
            tickets.append(row)
    return tickets


def summarize_tickets(tickets):
    counts = defaultdict(int)
    resolution_times = defaultdict(list)

    sla_totals = defaultdict(int)
    sla_met = defaultdict(int)
    sla_breached = defaultdict(int)

    tech_ticket_counts = defaultdict(int)
    tech_resolution_times = defaultdict(list)

    for t in tickets:
        issue = (t.get("Issue Type") or "Unknown").strip()
        status = (t.get("Status") or "").strip()
        rt_str = (t.get("Resolution Time (hours)") or "").strip()
        priority = (t.get("Priority") or "Unknown").strip()
        assigned_to = (t.get("Assigned To") or "Unassigned").strip()

        counts[issue] += 1
        tech_ticket_counts[assigned_to] += 1

        # Resolution time
        if status.lower() == "resolved" and rt_str:
            try:
                rt = float(rt_str)
                resolution_times[issue].append(rt)
                tech_resolution_times[assigned_to].append(rt)
            except ValueError:
                rt = None
        else:
            rt = None

        # SLA tracking
        if status.lower() == "resolved" and priority in SLA_RULES and rt is not None:
            sla_totals[priority] += 1
            if rt <= SLA_RULES[priority]:
                sla_met[priority] += 1
            else:
                sla_breached[priority] += 1

    # Averages
    averages = {issue: round(statistics.mean(times), 2) for issue, times in resolution_times.items()}
    tech_averages = {tech: round(statistics.mean(times), 2) for tech, times in tech_resolution_times.items()}

    sla_stats = {
        "totals": dict(sla_totals),
        "met": dict(sla_met),
        "breached": dict(sla_breached),
    }

    tech_stats = {
        "counts": dict(tech_ticket_counts),
        "averages": tech_averages,
    }

    return counts, averages, sla_stats, tech_stats


def print_report(counts, averages):
    print("=" * 60)
    print("Helpdesk Ticket Summary")
    print("=" * 60)
    print(f"{'Issue Type':<15} {'Ticket Count':<15} {'Avg Resolution (hrs)':<20}")
    print("-" * 60)

    all_issues = sorted(set(counts.keys()) | set(averages.keys()))
    for issue in all_issues:
        count = counts.get(issue, 0)
        avg = averages.get(issue, None)
        avg_str = f"{avg:.2f}" if isinstance(avg, float) else "N/A"
        print(f"{issue:<15} {count:<15} {avg_str:<20}")

    print("-" * 60)
    print(f"{'TOTAL':<15} {sum(counts.values()):<15}")
    print("=" * 60)


def print_sla_report(sla_stats):
    print()
    print("=" * 60)
    print("SLA Summary by Priority")
    print("=" * 60)
    print(f"{'Priority':<15} {'Total Resolved':<15} {'Met SLA':<10} {'Breached SLA':<15}")
    print("-" * 60)

    for priority in ["High", "Medium", "Low"]:
        total = sla_stats["totals"].get(priority, 0)
        met = sla_stats["met"].get(priority, 0)
        breached = sla_stats["breached"].get(priority, 0)
        print(f"{priority:<15} {total:<15} {met:<10} {breached:<15}")

    print("-" * 60)
    print("=" * 60)


def print_technician_report(tech_stats):
    print()
    print("=" * 60)
    print("Technician Performance Summary")
    print("=" * 60)
    print(f"{'Technician':<20} {'Ticket Count':<15} {'Avg Resolution (hrs)':<20}")
    print("-" * 60)

    for tech in sorted(tech_stats["counts"].keys()):
        count = tech_stats["counts"][tech]
        avg = tech_stats["averages"].get(tech)
        avg_str = f"{avg:.2f}" if isinstance(avg, float) else "N/A"
        print(f"{tech:<20} {count:<15} {avg_str:<20}")

    print("-" * 60)
    print("=" * 60)


def plot_counts(counts, chart_file):
    issues = sorted(counts.keys())
    values = [counts[i] for i in issues]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(issues, values, color="#3b82f6")
    plt.title("Tickets per Issue Type")
    plt.xlabel("Issue Type")
    plt.ylabel("Ticket Count")

    for bar, val in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(val),
                 ha="center", va="bottom")

    plt.tight_layout()
    plt.savefig(chart_file)
    print(f"Chart saved as: {chart_file}")


def plot_technician_counts(tech_stats, chart_file):
    technicians = sorted(tech_stats["counts"].keys())
    values = [tech_stats["counts"][t] for t in technicians]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(technicians, values, color="#10b981")
    plt.title("Tickets per Technician")
    plt.xlabel("Technician")
    plt.ylabel("Ticket Count")
    plt.xticks(rotation=30, ha="right")

    for bar, val in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(val),
                 ha="center", va="bottom")

    plt.tight_layout()
    plt.savefig(chart_file)
    print(f"Technician chart saved as: {chart_file}")


def main():
    tickets = load_tickets(CSV_FILE)

    if not tickets:
        print("No tickets found.")
        return

    counts, averages, sla_stats, tech_stats = summarize_tickets(tickets)

    print_report(counts, averages)
    print_sla_report(sla_stats)
    print_technician_report(tech_stats)

    plot_counts(counts, CHART_FILE)
    plot_technician_counts(tech_stats, TECH_CHART_FILE)


if __name__ == "__main__":
    main()
