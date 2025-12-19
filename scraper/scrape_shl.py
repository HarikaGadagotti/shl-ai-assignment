import requests
from bs4 import BeautifulSoup
import csv
import time

BASE_URL = "https://www.shl.com/products/product-catalog/"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def scrape_shl():
    results = []

    for start in range(0, 400, 16):
        url = f"{BASE_URL}?start={start}&type=1"
        print(f"Scraping: {url}")

        response = requests.get(url, headers=HEADERS, timeout=20)
        soup = BeautifulSoup(response.text, "html.parser")

        links = soup.select("a[href^='/products/']")

        if not links:
            print("⚠️ No links found on this page")
            continue

        for link in links:
            name = link.get_text(strip=True)
            href = link.get("href")

            if name and href:
                full_url = "https://www.shl.com" + href
                results.append({
                    "name": name,
                    "url": full_url
                })

        time.sleep(1)  # be polite

    print(f"Total assessments collected: {len(results)}")

    with open("data/shl_assessments.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "url"])
        writer.writeheader()
        writer.writerows(results)

    print("Saved to data/shl_assessments.csv")

if __name__ == "__main__":
    scrape_shl()
