
# Odds Portal scraping

This repository contains multiple scraping projects for Odds Portal.

Each one has its own `README.md` so just look in the directories, as detailed below.

Mainly `full_scraper/` is the most comprehensive and will cover most use cases.

**Note that all projects here were developed with Python 3.x and you should run/develop them with at least that**

| Directory name  | Description                                                                       |
|-----------------|-----------------------------------------------------------------------------------|
| `full_scraper`  | Will scrape nearly any sport and output as JSON. Most comprehensive and flexible. |
| `soccer_to_sql` | Scrapes soccer odds and scores then puts them in a SQLite database.               |
| `predictions`   | Scrapes predictions of users you follow - public or private - and saves them off. |


For This Fork:

run_save_to_csv.py is included in soccer_to_sql.
If you would like results to be saved into a comma separated value file, then use the run_save_to_csv.py 
if you would like the default option of saving to sqlite db, use the run.py 
