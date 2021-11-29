import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
from csv import writer

for i in range(0, 50):
    url = "https://www.amazon.com/Samsung-Chromebook-Celeron-Processor-Gigabit/product-reviews/B07XL4JHXR/ref=cm_cr_getr_d_paging_btm_next_3?ie=UTF8&reviewerType=all_reviews&pageNumber={i}.format(i=i)"
    response = requests.get(url, headers = { 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
    'Accept-Language' : 'en-US,en;q=0.5',
    'Accept-Encoding' : 'gzip', 
    'DNT' : '1',
    'Connection' : 'close'
    })

    soup = BeautifulSoup(response.text, 'html.parser')
    reviews = soup.find_all('div', {'data-hook': 'review'})

    with open('amazon_reviews.csv','w', newline='', encoding = 'utf8') as f:
        my_writer = writer(f)
        header = ["Title", "Rating", "Body"]
        my_writer.writerow(header)
        try:
            for item in reviews:
                title = item.find('a', {'data-hook':'review-title'}).text.strip()
                rating = float(item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip())
                body = item.find('span', {'data-hook': 'review-body'}).text.strip()

                row = [title, rating, body]

                my_writer.writerow(row)
        except:
            pass

