import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.candynation.com/sugar-free-candy?product_list_limit=30"
price_selector = "span.price"

csv_file = open("product_prices.csv", "w", newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Product Name", "Price"])

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.content, "html.parser")

products = soup.find_all("div", class_="product-item-info")
for product in products:
    name = product.find("a", class_="product-item-link").text.strip()
    price_elem = product.select_one(price_selector)  
    price = price_elem.text.strip() if price_elem else "N/A"

    csv_writer.writerow([name, price])

csv_file.close()  
print("Price data successfully scraped and saved to product_prices.csv")
