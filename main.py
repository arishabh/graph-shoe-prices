from time import time
from scrapping import *
from file_handler import *
from plot import *

shoes_url_path = "info/shoes_url.txt"
shoes_data_path = "info/shoes_data.txt"
stats_path = "info/stats.txt"
black_list_path = "info/black_list.txt"

max_time = 6 # No. of weeks you want the graph to show
frequency = 2 # Number of time you wantit to check in a day
max_no_of_urls = 70
black_list = read_file(black_list_path)

if __name__ == "__main__":
    main_start = time()#Start the time

    new_shoe_urls = scrapping_main() #Get all the latest URLS
    if(new_shoe_urls == None):
        exit()

    old_shoe_urls = read_file(shoes_url_path)
    merged_urls = merge(old_shoe_urls, new_shoe_urls, max_no_of_urls)
    for url in black_list:
        try:
            merged_urls.remove(url)
        except:
            continue
    write_file(shoes_url_path, merged_urls)#Put the merged urls in the file
    
    print("Total URls = " + str(len(merged_urls)))
    shoes_data=[]
    for url in merged_urls:
        start = time()
        data = scrapping_shoe(url)
        shoes_data.append(data) if data != None else black_list.append(url) 
        end = time()
        print("URL " + str(merged_urls.index(url)+1) + " took " + str(end-start) + " s")
    
    mid_end = time()
    mid_diff = mid_end-main_start
    print("Total time for scrapping: " + str(mid_diff/60) + " min")
    print("Took about " + str(mid_diff/(len(merged_urls)+1)) + " s per scrapping")
    
    append_file(shoes_data_path, shoes_data)
    write_file(black_list_path, black_list)

    all_data = shoes_data + read_file(shoes_data_path)
    processed_data = merge_shoes_data(all_data)
    plot_shoes(processed_data, max_time, frequency)
    
    main_end = time()
    text = "Total time for scrapping: " + str(mid_diff/60) + " min\n"
    text += "Time per scrape: " + str(mid_diff/(len(merged_urls)+1)) + " s\n"
    text += "Total Time taken: " + str((main_end-main_start)/60) + " min\n\n"
    append_file(stats_path, [text])
    print("Total time taken: " + str((main_end-main_start)/60) + " min")
