import requests
from bs4 import BeautifulSoup as bs
from RandomHeaders import LoadHeader
from scrapping import *
from file_handler import *

shoes_url_path = "info/shoes_url.txt"
shoes_data_path = "info/shoes_data.txt"

if __name__ == "__main__":
    new_shoe_urls = scrapping_main()
    if(new_shoe_urls == None):
        exit()
    old_shoe_urls = read_file(shoes_url_path)
    merged_urls = merge(old_shoe_urls, new_shoe_urls)
    write_list(shoes_url_path, merged_urls)
    
    shoes_data=[]
    all_shoe_urls = read_file(shoes_url_path)
    for url in all_shoe_urls:
        shoes_data.append(scrapping_shoe(url))

    write_list(shoes_data, shoes_data_path)
