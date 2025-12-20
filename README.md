## Helpdesk Ticket Automation (Python)
This project started as a way for me to practice Python by working with something familiar: helpdesk tickets. Since I deal with ticket data every day at work, I wanted to recreate a simple version of that workflow and see what I could do with it using basic scripting.

The script reads a CSV file of sample tickets, organizes the information, and generates a few summaries that you’d normally look at in a support environment. It also creates two charts that visualize the data. The goal wasn’t to build anything huge, just something practical that connects directly to the kind of work I already do.

## What the script does
The script loads a CSV file containing mock helpdesk tickets. Each ticket includes fields like issue type, status, assigned technician, priority, and resolution time. Once the data is loaded, the script:

• Summarizes ticket volume by issue type  
• Calculates average resolution times for resolved tickets  
• Tracks SLA performance based on priority levels  
• Breaks down technician performance (ticket counts + average resolution time)  
• Generates two charts:  
– ticket_summary.png (tickets by issue type)
– technician_ticket_counts.png (tickets per technician)

All of this is printed in the terminal and saved as images in the project folder.

## Why I built this
I wanted a small project that felt connected to my actual experience instead of something random. Working at the helpdesk, I’ve seen how useful it is to understand patterns in ticket data, which issues come up the most, how long things take to resolve, and how workload is distributed across the team.

Building this helped me practice Python in a hands‑on way. I learned how to read and clean data from a CSV file, work with dictionaries, calculate simple statistics, and generate charts. It also gave me a chance to think about things like SLAs and technician performance, which are real considerations in IT support.

## How to run it
If someone wants to try it out:

Install Python 3

Install matplotlib:

Code
pip install matplotlib
Run the script:

Code
python ticket_analysis.py
The script will print the summaries in the terminal and create the charts in the project folder.

Features included
- Ticket Summary  
Shows how many tickets fall under each issue type and the average resolution time for resolved tickets.

- SLA Tracking  
Uses simple rules (High/Medium/Low priority) to check whether resolved tickets met their expected resolution time.

- Technician Performance  
Counts how many tickets each technician handled and calculates their average resolution time.

- Charts  
Two visualizations are generated automatically:

Tickets per issue type

Tickets per technician

## What I might add later
There are a few things I’d like to experiment with if I keep building on this:

Tracking SLA breaches over time

Exporting summaries to Excel

Adding a simple command‑line menu

Highlighting recurring issues

Pulling data from an API instead of a CSV

Creating a small dashboard version

## Final notes

This project is intentionally simple, but it reflects how I think about support work and how I approach learning new tools. It helped me practice Python in a way that feels practical and gave me something concrete to share as I continue building out my skills.
