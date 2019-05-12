# libraries and data
import matplotlib.pyplot as plt
import pandas as pd
import time
import webScraping
import calculatePrime
import compression
import matplotlib


def lineGraph():

    webScrapingTimes = [webScraping.main(n) for n in range(1, 5)]
    calculatePrimeTimes = [calculatePrime.main(n) for n in range(1, 5)]
    compressionTimes = [compression.main(n) for n in range(1, 5)]

    #webScrapingTimes = [2.0918262004852295, 2.0087857246398926, 2.2411651611328125, 2.689840316772461]
    #calculatePrimeTimes = [8.845309257507324, 6.245893239974976, 5.476745367050171, 5.783617258071899]
    #compressionTimes = [1.0769598484039307, 1.1976118087768555, 1.461094617843628, 1.6775343418121338]

    # Make a data frame
    df = pd.DataFrame({'Milliseconds': range(1, 5), 'Web Scraping': webScrapingTimes,
                       'Calculating Primes': calculatePrimeTimes, 'Compression Times': compressionTimes})

    plt.style.use('seaborn-darkgrid')

    # create a color palette
    palette = plt.get_cmap('Set1')
    # multiple line plot
    num = 0
    for column in df.drop('Milliseconds', axis=1):
        num += 1
        plt.plot(df['Milliseconds'], df[column], marker='',
                 color=palette(num), linewidth=1, alpha=0.9, label=column)

    # Add legend
    plt.legend(loc=2, ncol=2)

    # Add titles
    plt.title("Testing Graph", loc='left', fontsize=12,
              fontweight=0, color='orange')
    plt.xlabel("Times run")
    plt.ylabel("Milliseconds")
    # plt.show()
    plt.savefig('picture.png')


def main():
    lineGraph()


if __name__ == '__main__':
    main()
