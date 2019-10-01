import matplotlib.pyplot as plt

def plot_shoes(info):
    info = info.split(" ")
    name = " ".join(info[:-7])
    base_price = int(info[-7][1:])
    lowest_ask_price = int(info[-6][1:])
    lowest_ask_size = int(info[-5])
    highest_bid_price = int(info[-4][1:])
    highest_bid_size = int(info[-3])
    release_date = info[-2]
    volatility = info[-1]
    print(name)
    print(base_price)
    print(lowest_ask_price)
    print(lowest_ask_size)
    print(highest_bid_price)
    print(highest_bid_size)
    print(release_date)
    print(volatility)

