import requests
from bs4 import BeautifulSoup as bs
from RandomHeaders import LoadHeader

shoes_url_file_path = "info/shoes_url.txt"

base_url = "https://www.stockx.com"
main_url = "https://stockx.com/sneakers/most-popular"

def scrapping():
    shoes_url=[]
    res = requests.get(base_url, headers=LoadHeader())
    res = requests.get(main_url, headers=LoadHeader())
    if(res.status_code == 200): #If made contact with website
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
    else:
        print("Couldnt connect to website...")
        return None

def readfile(new_file):
    text=[]
    with open(new_file, "r") as f: #Open file
        for line in f:
            line = line.strip(" ") # remove any empty spaces
            line = line.strip("\n") # remove new line charector
            text.append(line)
    return text

def merge(old_list, new_list): #merge both lists and removing duplicates
    for elem in new_list:
        if(elem not in old_list):
            old_list.append(elem)
    return old_list

if __name__ == "__main__":
    new_shoe_urls = scrapping()
    old_shoe_urls = readfile(shoes_url_file_path)
    if(new_shoe_urls == None):
        exit()
    merged_urls = merge(old_shoe_urls, new_shoe_urls)
    with open(shoes_url_file_path, "w") as f:
        for url in merged_urls:
            f.write(url + "\n")
