import matplotlib.pyplot as plt

plot_saves = "info/graphs/"

def plot_shoes(shoes_data):
    for data in shoes_data:
        print(data)
        
        lowest_ask = data[1][1:] if (len(data[1][1:])<20) else data[1][-5:]
        highest_bid =  data[2][1:] if (len(data[2][1:])<20) else data[2][-5:] 
        x_axis = list(range(len(lowest_ask)))
        print(lowest_ask, highest_bid)
        
        plt.figure(figsize=(12,10))
        plt.xlabel('Time (weeks)')
        plt.ylabel('Price ($)')
        plt.xlim(0,10)
        
        plt.plot(x_axis, lowest_ask, label='Lowest Ask Price', marker='o')
        plt.plot(x_axis, highest_bid, label='Highest Bid Price', marker='o')
        plt.axhline(data[0][1], color='r', label="Retail Price: $"+str(data[0][1]), linestyle='--')
        plt.title(data[0][0])
        plt.grid(color='grey', linestyle='--')
        
        plt.legend(loc='best')  # legend text comes from the plot's label parameter.
        for i in range(len(data[1][1:])):
            plt.text(x_axis[i]-0.2, (lowest_ask[i]+2), "$"+str(lowest_ask[i]), fontsize=13)
            plt.text(x_axis[i]-0.2, (highest_bid[i]+2), "$"+str(highest_bid[i]), fontsize=13)
        
        text = "Latest data:\n\n" + data[0][2] + "\nHighest Bid Price: $" + str(highest_bid[-1]) + " for Size: " + data[2][0] 
        text += "\nLowest Ask Price: $" + str(lowest_ask[-1]) + " for Size: " + data[1][0] + "\n" + data[0][3] + "\nRetail Price: $" +str(data[0][1])
        
        plt.text(11, (highest_bid[-1]+lowest_ask[-1])/2, text, fontsize=18)
        #plt.show()
        plt.savefig(plot_saves+(data[0][0].replace("/", "|"))+".png", bbox_inches="tight")
