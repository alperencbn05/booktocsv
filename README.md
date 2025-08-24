This project scrapes book title, price, and rating data from books.toscrape.com
 and saves the results into a CSV file.

🔧 Tech Stack

Python 3

requests → fetch HTML pages

BeautifulSoup (bs4) → parse HTML

pandas → build table & export CSV

🚀 Features

Handles pagination automatically (all 50 pages, ~1000 books)

Cleans data: price → float, rating → int (1–5)

Exports results to books.csv

📂 Example Output
title,price_gbp,rating
Sapiens: A Brief History of Humankind,54.23,5
Sharp Objects,47.82,4
A Light in the Attic,51.77,3

▶️ Usage
git clone https://github.com/alperencbn05/booktocsv.git
cd booktocsv
pip install -r requirements.txt
python main.py
