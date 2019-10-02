def read_file(file_path):
    content=[]
    with open(file_path, "r") as f: #Open file
        for line in f:
            line = line.strip(" ") # remove any empty spaces
            line = line.strip("\n") # remove new line charector
            content.append(line)
    return content

def merge(old_list, new_list): #merge both lists and removing duplicates
    for elem in new_list:
        if(elem not in old_list):
            old_list.append(elem)
    return old_list

def write_list(file_path, file_list): #Write the given list on a file
    with open(file_path, "w") as f:
        for data in file_list:
            f.write(data + "\n")

def merge_shoe_data(inp_list):
    data = []
    for line in inp_list:
        line = line.split(" ")
        name = " ".join(line[:-7])
        lowest_ask_price = line[-6][1:]
        lowest_ask_size = "Size: " + line[-5]
        highest_bid_price = line[-4][1:]
        highest_bid_size = "Size: " + line[-3]
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
            base_price = "Retail Price: " + line[-7][1:]
            release_date = "Release Date: " + line[-2]
            data.append([[name, base_price, release_date, volatility], 
                [lowest_ask_size, lowest_ask_price],
                [highest_bid_size, highest_bid_price]])
    
    return data
