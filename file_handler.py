def read_file(file_path):
    content=[]
    with open(file_path, "r") as f: #Open file
        for line in f:
            line = line.strip(" ") # remove any empty spaces
            line = line.strip("\n") # remove new line charector
            content.append(line)
    return content

def merge(old_list, new_list, max_urls): #merge both lists and removing duplicates
    new_urls = []
    for elem in new_list:
        if(elem not in old_list):
            old_list.append(elem)
            new_urls.append(elem)
        else:
            old_list.remove(elem)
            old_list.append(elem)
    return old_list if (len(old_list) <= max_urls) else old_list[:max_urls]

def write_file(file_path, file_list): #Write the given list on a file
    with open(file_path, "w") as f:
        for data in file_list:
            f.write(data + "\n")
    return

def append_file(file_path, file_list):
    with open(file_path, "a") as f:
        for data in file_list:
            f.write(data + "\n")

def merge_shoes_data(inp_list):
    data = []
    for line in inp_list:
        line = line.split(" ")
        name = " ".join(line[:-8])
        shoe_url = line[-8]
        lowest_ask_price = int(line[-6])

        lowest_ask_size = line[-5]
        highest_bid_price = int(line[-4])
        highest_bid_size = line[-3]
        volatility = "Volatility: " + line[-1]
        flag = False
        for index in range(len(data)):
            if(data[index][0][0] == name):
                data[index][0][-1] = volatility
                data[index][1][0] = lowest_ask_size
                data[index][1].append(lowest_ask_price)
                data[index][2][0] = highest_bid_size
                data[index][2].append(highest_bid_price)
                flag = True
            if(flag): break
        if(not flag):
            base_price = int(line[-7])
            release_date = "Release Date: " + line[-2]
            data.append([[name, base_price, release_date, volatility, shoe_url], 
                [lowest_ask_size, lowest_ask_price],
                [highest_bid_size, highest_bid_price]])
    
    return data
#Ex output = [[['adidas shoe', '160', '10/4/2019', '28%', 'www.stockx.com/adidas/shoe], ['5', 200, 205], ['10', 300, 330]],
#              ['jordan shoe2', '150', '12/4/2019', '8%', 'www.stockx.com/jordan/shoe2'], ['15', 240, 205], ['9', 250, 230]]]

def clear_file(file_path):
    with open(file_path, "w") as f:
        f.write("")
    return
