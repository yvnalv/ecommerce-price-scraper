from bs4 import BeautifulSoup

def parse_products(html):
    soup = BeautifulSoup(html, "html.parser")
    container = soup.select_one(".grid.grid-cols-2")
    if not container:
        return []

    product_cards = container.find_all("div", class_="card-product")
    products = []

    for card in product_cards:
        name_tag = card.find("h2")
        price_tag = card.find("div", class_="price")
        if name_tag and price_tag:
            products.append({
                "name": name_tag.text.strip(),
                "price": price_tag.text.strip()
            })
    return products
