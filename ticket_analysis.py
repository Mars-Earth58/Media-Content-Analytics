import csv
from collections import defaultdict
import statistics
import matplotlib.pyplot as plt

# File names
CSV_FILE = "tickets.csv"
CHART_FILE = "ticket_summary.png"


def load_tickets(csv_file):
    tickets = []
    with open(csv_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Skip completely empty rows
            if not any(row.values()):
                continue
            tickets.append(row)
    return tickets


def summarize_tickets(tickets):
    counts = defaultdict(int)
    resolution_times = defaultdict(list)

    for t in tickets:
        # Safely get values even if keys are missing or None
        issue_raw = t.get("Issue Type")
        issue = (issue_raw or "Unknown").strip() or "Unknown"

        status_raw = t.get("Status")
        status = (status_raw or "").strip()

        rt_raw = t.get("Resolution Time (hours)")
        rt_str = (rt_raw or "").strip()

        counts[issue] += 1

        # Only count resolution time when resolved and a numeric value exists
        if status.lower() == "resolved" and rt_str:
            try:
                resolution_times[issue].append(float(rt_str))
            except ValueError:
                # Ignore bad numeric values
                pass

    # Compute averages safely
    averages = {}
    for issue, times in resolution_times.items():
        averages[issue] = round(statistics.mean(times), 2) if times else None

    return counts, averages


def print_report(counts, averages):
    print("=" * 60)
    print("Helpdesk Ticket Summary")
    print("=" * 60)
    print(f"{'Issue Type':<15} {'Ticket Count':<15} {'Avg Resolution (hrs)':<20}")
    print("-" * 60)

    all_issues = sorted(set(list(counts.keys()) + list(averages.keys())))
    for issue in all_issues:
        count = counts.get(issue, 0)
        avg = averages.get(issue)
        avg_str = f"{avg:.2f}" if isinstance(avg, float) else "N/A"
        print(f"{issue:<15} {count:<15} {avg_str:<20}")

    print("-" * 60)
    total = sum(counts.values())
    print(f"{'TOTAL':<15} {total:<15}")
    print("=" * 60)


def plot_counts(counts, chart_file):
    if not counts:
        print("No ticket data available to plot.")
        return

    issues = sorted(counts.keys())
    values = [counts[i] for i in issues]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(issues, values, color="#3b82f6")
    plt.title("Tickets per Issue Type")
    plt.xlabel("Issue Type")
    plt.ylabel("Ticket Count")

    for bar, val in zip(bars, values):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.05,
            str(val),
            ha="center",
            va="bottom",
            fontsize=9,
        )

    plt.tight_layout()
    plt.savefig(chart_file)
    print(f"Chart saved as: {chart_file}")


def main():
    try:
        tickets = load_tickets(CSV_FILE)
    except FileNotFoundError:
        print(f"ERROR: Could not find '{CSV_FILE}'. Make sure it exists in this folder.")
        return

    if not tickets:
        print("No tickets found in the CSV file.")
        return

    counts, averages = summarize_tickets(tickets)
    print_report(counts, averages)
    plot_counts(counts, CHART_FILE)


if __name__ == "__main__":
    main()

