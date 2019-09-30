def readfile(file_path):
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