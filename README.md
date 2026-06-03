# Web scraping — ProductHunt, GitHub & Google Play with Python

Different targets, different techniques — chosen based on each site's technical constraints.

## Approach 1 — GitHub (requests + BeautifulSoup)

GitHub search pages render server-side, so a simple HTTP request is enough.
Tools: `requests`, `BeautifulSoup`, `json`
File: `web_scraping.py`

## Approach 2 — ProductHunt (Selenium + BeautifulSoup)

ProductHunt uses client-side JavaScript rendering — simple requests return empty pages.
Solution: automate a real browser with Selenium to let the page load before parsing.
Tools: `selenium`, `BeautifulSoup`, `json`, `csv`
Files : `producthuntlab2.py`,`products.json`,`products.csv`

## Approach 3 — Google Play (API via google-play-scraper)

Instead of scraping the HTML, this approach uses an API-style library to pull
structured data directly. Cleaner and more reliable than parsing pages.
Used here to collect data on mental health & wellness apps, including their
user reviews, and store everything in a JSON file.
Tools: `google-play-scraper`, `json`
Files: `lab1_scraperapi.py` → output: `wellness_apps_data.json`

