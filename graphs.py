# libraries and data
import matplotlib.pyplot as plt
import pandas as pd
import time
import webScraping
import calculatePrime
import compression
import matplotlib
import encoding
import mysort

def lineGraph():

    webScrapingTimes = [webScraping.main(n) for n in [1,3,5,7,10,13,16]]
    calculatePrimeTimes = [calculatePrime.main(n) for n in [1,3,5,7,10,13,16]]
    compressionTimes = [compression.main(n) for n in [1,3,5,7,10,13,16]]
    encodingTimes = [encoding.main(n) for n in [1,3,5,7,10,13,16]]
    sortingTimes = [mysort.main(n) for n in [1,3,5,7,10,13,16]]
    
    # Make a data frame
    df = pd.DataFrame({'Seconds': [1,3,5,7,10,13,16], 'Web Scraping': webScrapingTimes,
                       'Calculate Primes': calculatePrimeTimes, 'Compression': compressionTimes, 'Encoding':encodingTimes, 'Sorting': sortingTimes})

    plt.style.use('seaborn-darkgrid')

    # create a color palette
    palette = plt.get_cmap('Set1')
    # multiple line plot
    num = 0
    for column in df.drop('Seconds', axis=1):
        num += 1
        plt.plot(df['Seconds'], df[column], marker='',
                 color=palette(num), linewidth=1, alpha=0.9, label=column)

    # Add legend
    plt.legend(loc=2, ncol=2)

    # Add titles
    plt.title("Multiprocessing Test", loc='left', fontsize=12,
              fontweight=0, color='orange')
    plt.xlabel("Processes")
    plt.ylabel("Seconds")
    plt.savefig('picture.png')


def main():
    lineGraph()


if __name__ == '__main__':
    main()
