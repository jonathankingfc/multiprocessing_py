# libraries and data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
import webScraping
import calculatePrime
import compression


def lineGraph():
    webScrapingTimes = [webScraping.main(n) for n in range(1, 5)]
    calculatePrimeTimes = [calculatePrime.main(n) for n in range(1, 5)]
    compressionTimes = [compression.main(n) for n in range(1, 5)]

    df = pd.DataFrame({'Web_Scraping': webScrapingTimes,
                       'Calculating Primes': calculatePrimeTimes,
                       'Compressing Text': compressionTimes},
                      index=list(range(1, 5)))
    print(df.head())
    

#     # style
    plt.style.use('seaborn-darkgrid')
    plt.xlim(0,10)
    plt.ylim(0,10)

#     # create a color palette
#     palette = plt.get_cmap('Set1')

#     # multiple line plot
#     num=0
#     for column in df.drop('x', axis=1):
#         num+=1
    plt.plot(y = df['Web_Scraping'], x = 'index', linewidth=1)
    plt.savefig("picture.png")
#     plt.plot(df['y1'], df[column], marker='', color=palette(num), linewidth=1, alpha=0.9, label=column)
#     plt.plot(df['y2'], df[column], marker='', color=palette(num), linewidth=1, alpha=0.9, label=column)


#     # Add legend
#     plt.legend(loc=2, ncol=2)

#     # Add titles
#     plt.title("Testing Graph", loc='left', fontsize=12, fontweight=0, color='orange')
#     plt.xlabel("X")
#     plt.ylabel("Y")
#     plt.show()

# def barGraph():
#     # Make a fake dataset:
#     height = [3, 12, 5, 18, 45]
#     bars = ('A', 'B', 'C', 'D', 'E')
#     y_pos = np.arange(len(bars))

#     # Create bars
#     plt.bar(y_pos, height)

#     # Create names on the x-axis
#     plt.xticks(y_pos, bars)

#     # Show graphic
#     plt.show()

def main():
    lineGraph()


if __name__ == '__main__':
    main()
