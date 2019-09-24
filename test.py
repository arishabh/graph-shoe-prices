import requests
from bs4 import BeautifulSoup as bs
from RandomHeaders import LoadHeader

stockx = "https://www.stockx.com"
ex = "https://stockx.com/adidas-yeezy-boost-350-v2-cream-white"
ex_sell = "https://stockx.com/sell/adidas-yeezy-boost-350-v2-cream-white"
ex_buy = "https://stockx.com/buy/adidas-yeezy-boost-350-v2-cream-white"
header = LoadHeader()

def startup():
    res = requests.get(stockx, headers=header)
    res = requests.get(ex, headers=header) 
    res1 = requests.get(ex_buy, headers=header)
    res2 = requests.get(ex_sell, headers=header)
    cont = bs(res.text, "lxml")
    buy = bs(res1.text, "lxml")
    sell = bs(res2.text, "lxml")
    return cont, buy, sell
