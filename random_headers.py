import random
import csv


headers_csv = open('Headers.csv', 'r')
headers_list = csv.reader(headers_csv)
headers_list = [row for row in headers_list]
headers_list = [l[0] for l in headers_list]
random.shuffle(headers_list)

def LoadHeader():
	return {'User-Agent': random.choice(headers_list).strip(" ")}
