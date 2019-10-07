import matplotlib.pyplot as plt
import math

plot_saves = "info/graphs/"

def plot_shoes(shoes_data, max_time, freq):
    for data in shoes_data:
        #print(data)
        
        num_data = 7*freq*max_time
        lowest_ask = data[1][1:] if (len(data[1][1:])<num_data) else data[1][num_data*-1:]
        highest_bid =  data[2][1:] if (len(data[2][1:])<num_data) else data[2][num_data*-1:] 
        
        peak_price = max(data[2][1:])

        x_coef = 1/num_data
        x_axis = []
        for i in range(len(lowest_ask)):
            x_axis.append(i*x_coef)
        
        #print(lowest_ask, highest_bid)
        
        plt.figure(figsize=(15,13))
        plt.xlabel('Time (weeks)')
        plt.ylabel('Price ($)')
        plt.xlim(0,math.ceil(x_axis[-1])) #Optional
        
        plt.plot(x_axis, lowest_ask, label='Lowest Ask Price')
        plt.plot(x_axis, highest_bid, label='Highest Bid Price')
        plt.axhline(data[0][1], color='r', label="Retail Price: $"+str(data[0][1]), linestyle='--')
        plt.title(data[0][0])
        plt.grid(color='grey', linestyle='--')
        plt.legend(loc='best')  # legend text comes from the plot's label parameter.
              
        y_bot, y_top = plt.ylim()
        x_min, x_max = plt.xlim()
        y_diff = y_top - y_bot
        x_diff = x_max - x_min
        
        x_dist = 2*x_diff/100
        y_dist = y_diff/100
        y_pos_text = (y_bot+y_top)/2
        x_pos_text = x_max + x_diff/5
        
        plt.text(x_axis[-1]-x_dist, (lowest_ask[-1]+y_dist), "$"+str(lowest_ask[-1]), fontsize=13)
        plt.text(x_axis[-1]-x_dist, (highest_bid[-1]+y_dist), "$"+str(highest_bid[-1]), fontsize=13)

        """
        start = -5 if len(x_axis)>=5 else len(x_axis)
        for i in range(start, 0, 1):
            plt.text(x_axis[i]-x_dist, (lowest_ask[i]+y_dist), "$"+str(lowest_ask[i]), fontsize=13)
            plt.text(x_axis[i]-x_dist, (highest_bid[i]+y_dist), "$"+str(highest_bid[i]), fontsize=13)
        """
        text = "Latest data:\n\n" + data[0][2] + "\nHighest Bid Price: $" + str(highest_bid[-1]) + " for Size: " + data[2][0] 
        text += "\nLowest Ask Price: $" + str(lowest_ask[-1]) + " for Size: " + data[1][0] + "\n" + data[0][3] + "\nRetail Price: $" +str(data[0][1]) + "\nPeak Price: $" + str(peak_price)
        
        plt.text(x_pos_text, y_pos_text, text, fontsize=18)
        #plt.show()
        plt.savefig(plot_saves+data[0][0]+".png", bbox_inches="tight")
