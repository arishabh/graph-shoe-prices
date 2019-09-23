import requests
from bs4 import BeautifulSoup as bs
from random_headers import LoadHeader

temp_url = "https://www.stockx.com"
res = requests.get(temp_url, headers=LoadHeader())
main_url = "https://stockx.com/sneakers/most-popular"
res = requests.get(main_url, headers=LoadHeader())
if(res.status_code == 200):
    s = bs(res.content, "lxml")
    for a in s.findAll("a", href=True):
        print(a['href'])
