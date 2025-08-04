# Daily Metrics Bot

This is a simple GitHub bot that **automatically updates a JSON file (`metrics.json`) every day** by incrementing three numeric values. The process is fully automated using **GitHub Actions** and requires no manual execution.

---


## What It Does


- Reads a file called `metrics.json` in the repository.
- Increments three numeric values (`metric1`, `metric2`, `metric3`) by **1** each day.
- Commits and pushes the updated file back to the repository automatically.
- Runs **daily at 9:00 AM Afghanistan time**.


