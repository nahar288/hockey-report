import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {"User-Agent": "Mozilla/5.0"}
all_data = []
for i in range(1, 6):

    url = f"https://www.scrapethissite.com/pages/forms/?page_num={i}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.find_all("tr", class_="team")

    