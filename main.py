from time import time
from scrapping import *
from file_handler import *
from plot import *

shoes_url_path = "info/shoes_url.txt"
shoes_data_path = "info/shoes_data.txt"
black_list = []

max_time = 6 # No. of weeks you want the graph to show
frequency = 2 # Number of time you wantit to check in a day

if __name__ == "__main__":
    main_start = time()#Start the time

    new_shoe_urls = scrapping_main() #Get all the latest URLS

    if(new_shoe_urls == None):
        exit()

    old_shoe_urls = read_file(shoes_url_path)
    merged_urls = merge(old_shoe_urls, new_shoe_urls)
    for url in black_list:
        try:
            merged_urls.remove(url)
        except:
            continue
    write_list(shoes_url_path, merged_urls)#Put the merged urls in the file
    
    print("Total URls = " + str(len(merged_urls)))
    shoes_data=[]
    for url in merged_urls:
        start = time()
        data = scrapping_shoe(url)
        shoes_data.append(data) if data != None else black_list.append(url) 
        end = time()
        print("URL " + str(merged_urls.index(url)+1) + " took " + str(end-start) + " s")
    mid_end = time()
    print("Total time for scrapping: " + str((mid_end-main_start)/60) + " min")
    print("Took about " + str((mid_end-main_start)/(len(merged_urls)+1)) + " s per scrapping")
    
    old_data = read_file(shoes_data_path)
    all_data = old_data + shoes_data
    write_list(shoes_data_path, all_data)

    plot_shoes(merge_shoes_data(all_data), max_time, frequency)
    main_end = time()
    print("Total time taken: " + str((main_end-main_start)/60) + " min")
