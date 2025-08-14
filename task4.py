import requests
from bs4 import BeautifulSoup
import csv

# Target website (safe for scraping)
url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"

# Send GET request
response = requests.get(url)
if response.status_code != 200:
    print("Failed to retrieve the webpage")
    exit()

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all product containers
products = soup.find_all("div", class_="thumbnail")

# Prepare CSV file
with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price", "Rating"])

    for product in products:
        # Extract product name
        name_tag = product.find("a", class_="title")
        name = name_tag.text.strip() if name_tag else "N/A"

        # Extract price
        price_tag = product.find("h4", class_="pull-right price")
        price = price_tag.text.strip() if price_tag else "N/A"

        # Extract rating
        rating_tag = product.find("div", class_="ratings")
        rating_p = rating_tag.find("p", class_="pull-right") if rating_tag else None
        rating = rating_p.text.strip() if rating_p else "N/A"

        # Write to CSV
        writer.writerow([name, price, rating])

print("✅ Scraping complete! Data saved in products.csv")
