# main.py
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys


HEADERS = {"User-Agent": "Mozilla/5.0 (educational scraping)"}
BASE_URL = "http://books.toscrape.com/"  


rating_map = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5}

def get_html(url: str) -> str:
    r = requests.get(url, headers=HEADERS, timeout=10)
    r.encoding = "utf-8"
    r.raise_for_status()
    return r.text

def parse_books(html: str):
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for b in soup.select("article.product_pod"):
        title = b.find("h3").find("a")["title"]
        price_txt = b.select_one("p.price_color").text.strip().replace("£","").replace("Â","")
        price = float(price_txt)
        rating_txt = b.select_one("p.star-rating")["class"][1]
        rating = rating_map[rating_txt]
        rows.append({"title": title, "price_gbp": price, "rating": rating})
    return rows

def get_next_page_url(html: str, base_url: str):
    soup = BeautifulSoup(html, "html.parser")
    a = soup.select_one("li.next > a")
    return urljoin(base_url, a["href"]) if a else None

if __name__ == "__main__":
    url = BASE_URL
    all_rows = []
    while url:
        html = get_html(url)
        page_rows = parse_books(html)
        all_rows.extend(page_rows)
        print(f"TOTAL: {len(all_rows)} | {url}")
        url = get_next_page_url(html, url)
        time.sleep(0.6)

    pd.DataFrame(all_rows, columns=["title","price_gbp","rating"]).to_csv(
        "books.csv", index=False, encoding="utf-8"
    )
    print("✅ books.csv hazır.")
    sys.exit(0)
