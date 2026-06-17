from dotenv import load_dotenv
import os
import httpx
from bs4 import BeautifulSoup as bs

load_dotenv()
link = os.getenv("LINK_PROFILE")
profil = os.getenv("PROFILE")
def getcredit(link , profile):
    r = httpx.get(f"{link}/{profile}")
    data = bs(r.content , "html.parser")
    if r.status_code == 200:
        a = data.select_one('a[href*="dbtech-credits/currency/credits.1"]')
        print(a.text.strip())





