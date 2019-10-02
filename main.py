from time import time
from scrapping import *
from file_handler import *

shoes_url_path = "info/shoes_url.txt"
shoes_data_path = "info/shoes_data.txt"

if __name__ == "__main__":
    main_start = time()#Start the time

    new_shoe_urls = scrapping_main() #Get all the latest URLS

    if(new_shoe_urls == None):
        exit()

    old_shoe_urls = read_file(shoes_url_path)
    merged_urls = merge(old_shoe_urls, new_shoe_urls)
    write_list(shoes_url_path, merged_urls)#Put the merged urls in the file
    
    shoes_data=[]
    for url in merged_urls:
        start = time()
        data = scrapping_shoe(url)
        shoes_data.append(data) if data != None else print("Got None\n") 
        end = time()
        print("URL " + str(all_shoe_urls.index(url)+1) + " took " + str(end-start) + "s")
    
    old_data = read_file(shoes_data_path)
    all_data = old_data + shoes_data
    write_list(shoes_data_path, all_data)
    main_end = time()
    print("Total time taken: " + str((main_end-main_start)/60) + "min")
    print("Took about " + str((main_end-main_start)/(len(all_shoe_urls)+1)) + "s per scrapping")
