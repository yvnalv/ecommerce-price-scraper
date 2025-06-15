import logging
from scraper import config, fetcher, parser, saver

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

def main():
    query = "kopi"
    category = config.DEFAULT_CATEGORY
    all_products = []

    driver = fetcher.init_driver()

    for page in range(1, config.MAX_PAGES + 1):
        url = config.SEARCH_URL_TEMPLATE.format(query=query, category=category, page=page)
        logging.info(f"Scraping page {page}: {url}")
        html = fetcher.fetch_page_source(driver, url)
        products = parser.parse_products(html)

        if not products:
            logging.info("No more products found, stopping pagination.")
            break

        all_products.extend(products)

    driver.quit()

    logging.info(f"Total products scraped: {len(all_products)}")
    saver.save_to_csv(all_products, config.OUTPUT_CSV_PATH)
    logging.info(f"Saved products to {config.OUTPUT_CSV_PATH}")

if __name__ == "__main__":
    main()
