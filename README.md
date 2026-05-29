#Web scraping — ProductHunt & GitHub with Python

Two targets, two different techniques — chosen based on each site's technical constraints.

## Approach 1 — GitHub (requests + BeautifulSoup)
GitHub search pages render server-side, so a simple HTTP request is enough.
Tools: `requests`, `BeautifulSoup`, `json`

## Approach 2 — ProductHunt (Selenium + BeautifulSoup)
ProductHunt uses client-side JavaScript rendering — simple requests return
empty pages. Solution: automate a real browser with Selenium to let the
page load before parsing.
Tools: `selenium`, `BeautifulSoup`, `json`, `csv`

