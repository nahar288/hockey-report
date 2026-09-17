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

    for r in rows:
        team = r.find("td", class_="name")
        year = r.find("td", class_="year")
        wins = r.find("td", class_="wins")
        losses = r.find("td", class_="losses")
        ot_losses = r.find("td", class_="ot-losses")
        win_pct = r.find("td", class_="pct")
        goals_for = r.find("td", class_="gf")
        goals_against = r.find("td", class_="ga")
