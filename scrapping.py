import requests
from bs4 import BeautifulSoup as bs
from RandomHeaders import *

TOTAL_TRIES = 5
tries = 0

base_url = "https://www.stockx.com"
main_url = "https://www.stockx.com/sneakers/most-popular"

header = ""

def base_soup():
    tried = 0
    status = 0
    while((status != 200) or (tries <= TOTAL_TRIES)):
        header = LoadHeader()
        res = requests.get(base_url, headers=header)
        status = res.status_code
        tries += 1


def soup(url):
    tries = 0
    status = 0
    while((status != 200)  or (tries <= TOTAL_TRIES)): #Try with different headers 5 times
        header = LoadHeader()
        res = requests.get(url, headers=header)
        status = res.status_code
        tries += 1
    
    if(res.status_code != 200):
        print("Couldnt connect to website...")
        return None
    
    s = bs(res.content, "lxml") #Convert into beautiful soup 
    print(header)
    return s

def scrapping_main():
    shoes_url=[]
    s = soup(main_url)
    for a in s.findAll("a", href=True): #All the href values
        if(a['href'] != "/"): #If not empty url
            shoes_url.append(a['href']) #Put them in an array

    url_len = len(shoes_url)
    #Remove URL for unwanted things
    shoes_url = shoes_url[25:url_len-67] 
    for index in range(len(shoes_url)):
        shoes_url[index] = base_url + shoes_url[index]
    return shoes_url

def scrapping_shoe(shoe_url): #Need base, lowest ask and highest bid prices, valatility and release date
    content = soup(shoe_url)
    
    shoe_name = content.title.string.split(" - ")[0]

    bids = content.findAll("div", {"class": "en-us stat-value stat-small"})
    if (bids == []): return None
    lowest_ask = bids[0].text[1:]
    highest_bid = bids[1].text[1:]
    
    sizes = content.findAll("span", {"class": "bid-ask-sizes"})
    lowest_ask += " " + (sizes[0].text).split(" ")[1] #Adding the sizes
    highest_bid += " " + (sizes[1].text).split(" ")[1] 
    #print(lowest_ask + highest_bid)

    base_price = content.findAll("span", {"class":"sneak-score"})[1].text[2:]
    spans=content.findAll("span")
    volatility = None
    release_date = None
    for index in range(len(spans)):
        if (spans[index].text == "Release Date"):
            release_date = spans[index+1].text.strip(" ")
        if (spans[index].text == "Volatility"):
            volatility = spans[index+1].text
    if ((volatility is None) or (release_date is None)): return None 
    return " ".join([shoe_name, base_price, lowest_ask, highest_bid, release_date, volatility])
