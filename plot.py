import matplotlib.pyplot as plt

def plot_shoes(shoes_data):
    for data in shoes_data:
        print(data)
        x_axis = list(range(len(data[1][1:])))
        plt.plot(x_axis, data[1][1:], label='Lowest Ask Price')
        plt.plot(x_axis, data[2][1:], label='Highest Bid Price')
        plt.axhline(data[0][1], color='r', label="Retail Price", linestyle='--')
        plt.title(data[0][0])
        plt.grid(color='grey', linestyle='--')
        plt.text(x=0,y=10,s="Hey", fontsize=20)
        plt.xlabel('Time (weeks)')
        plt.ylabel('Price ($)')
        plt.legend(loc='best')  # legend text comes from the plot's label parameter.
        plt.show()
