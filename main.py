from time import time
from scrapping import *
from file_handler import *
from plot import *

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
    
    print("Total URls = " + str(len(merged_urls)))
    shoes_data=[]
    for url in merged_urls:
        start = time()
        data = scrapping_shoe(url)
        shoes_data.append(data) if data != None else print("\nCouldnt connect to URL below") 
        end = time()
        print("URL " + str(merged_urls.index(url)+1) + " took " + str(end-start) + " s")
    mid_end = time()
    print("Total time for scrapping: " + str((mid_end-main_start)/60) + " min")
    print("Took about " + str((mid_end-main_start)/(len(merged_urls)+1)) + " s per scrapping")
    
    old_data = read_file(shoes_data_path)
    all_data = old_data + shoes_data
    write_list(shoes_data_path, all_data)

    plot_shoes(merge_shoes_data(all_data))
    main_end = time()
    print("Total time taken: " + str((main_end-main_start)/60) + " min")
