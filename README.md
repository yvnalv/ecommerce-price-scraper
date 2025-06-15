# ☕ KlikIndomaret Coffee Scraper & Dashboard

This project scrapes coffee product listings from [KlikIndomaret.com](https://klikindomaret.com), saves the data to CSV, and displays it in a Streamlit dashboard with filtering and price insights.

## Extracted Fields
- Product Name
- Price
- Category
- Link (optional if added later)

## Features
- Pagination handling for deeper scraping
- Category filter support
- Headless Selenium for JS-rendered content
- Docker support for deployment
- Streamlit dashboard with:
  - Search by name
  - Filter by category
  - Price distribution chart
  - Summary statistics

## Tools Used
- Python
- Selenium
- BeautifulSoup
- pandas
- Streamlit
- Docker

## Sample Output

| Name                      | Price       |
|---------------------------|-------------|
| Kopi ABC Susu 31g         | Rp2.000     |
| Nescafé Classic 100g      | Rp26.500    |
| Luwak White Koffie 10s    | Rp12.000    |

## Legal Notice
This project is for educational and portfolio use only. Data is obtained from a public website using responsible scraping techniques with respect to fair use policies.
