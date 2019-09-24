import requests
from bs4 import BeautifulSoup as bs

TOTAL_TRIES = 5
tries = 0

base_url = "https://www.stockx.com"
main_url = "https://www.stockx.com/sneakers/most-popular"

def scrapping_main():
    tries = 0
    shoes_url=[]
    status = 0
    while((status != 200)  or (tries <= TOTAL_TRIES)): #Try with different headers 5 times
        res = requests.get(base_url, headers=LoadHeader())
        res = requests.get(main_url, headers=LoadHeader())
        status = res.status_code()
        tires += 1
    
    if(res.status_code != 200):
        print("Couldnt connect to website...")
        return None
    
    s = bs(res.content, "lxml") #Convert into beautiful soup 
    for a in s.findAll("a", href=True): #All the href values
        if(a['href'] != "/"): #If not empty url
            shoes_url.append(a['href']) #Put them in an array

    url_len = len(shoes_url)
    #Remove URL for unwanted things
    shoes_url = shoes_url[25:url_len-67] 
    for index in range(len(shoes_url)):
        shoes_url[index] = base_url + shoes_url[index]
    return shoes_url

def scrapping_shoe(shoe_url):
    buy_url = shoe_url[:23] + "buy/" + shoe_url[23:len(shoe_url)]
    sell_url = shoe_url[:23] + "sell/" + shoe_url[23:len(shoe_url)]
    
