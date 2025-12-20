## Helpdesk Ticket Automation (Python)
This project started as a small way for me to practice Python and get more comfortable with basic automation. Since I work with tickets every day at the helpdesk, I wanted to recreate a simple version of that workflow using a CSV file and a short script. The goal wasn’t to build anything complex, but to build something realistic that connects to the kind of work I already do.

The script reads a CSV file of sample helpdesk tickets, organizes the data, and gives a quick summary of what types of issues are coming in and how long they take to resolve. It also generates a chart that shows the number of tickets by issue type. This is the kind of quick analysis that can be useful when you’re trying to understand patterns, spot recurring problems, or explain workload trends to a team.

## What the script does
The script loads a CSV file containing mock ticket data. Each row represents a ticket with fields like issue type, status, assigned technician, and resolution time. Once the data is loaded, the script:

Counts how many tickets fall under each issue type

Calculates the average resolution time for issues that have been resolved

Prints a summary in the terminal

Creates a bar chart called ticket_summary.png showing ticket counts by category

The idea was to simulate the kind of small reporting task you might do when looking at helpdesk activity over a day or week.

## Why I built this
I wanted a project that felt connected to my actual experience instead of something random. Working at the helpdesk, I’ve seen how useful it is to understand ticket patterns, whether certain issues are happening more often, whether resolution times are improving, and how workload is distributed across categories.

This project gave me a chance to practice Python in a way that feels practical. It helped me understand how to read data from a file, work with dictionaries, calculate simple statistics, and generate a chart. It also helped me get more comfortable organizing a small project and writing code that someone else could read and run.

## How to run it
If someone wants to try it out, here’s the simplest way:

Install Python 3

Install matplotlib:

Code
pip install matplotlib
Run the script:

Code
python ticket_analysis.py
The script will print a summary in the terminal and create a chart in the project folder.

## What I might add later
If I keep building on this, I’d like to experiment with a few things:

Tracking SLA deadlines

Highlighting overdue or high‑priority tickets

Exporting the summary to Excel

Adding a simple menu so you can choose what kind of report to generate

Pulling data from an API instead of a CSV

These aren’t necessary for the basic version, but they’d be good ways to keep learning.

## Final notes
This project 
reflects how I think about support work and how I approach learning new tools. It helped me practice Python in a hands‑on way and gave me something concrete to share as I continue building out my skills.
