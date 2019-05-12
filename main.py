import webScraping
import calculatePrime
import binarySort
import compression
import encoding
import argparse
import sys


def main():
    print("\n================================================================================\nWelcome to our program! We will be testing the multiprocessing module on various workloads.")
    while(True):
        option = int(input(
            "\nPlease select from the following: \n"
            "1. Web Scraping\n"
            "2. Calculating Primes\n"
            "3. Compressing Text Files\n"
            "4. Encoding Image Files\n"
            "5. Sorting Algorithms\n"
            "6. Show Graph\n"
            "7. Quit Program\n"
            "Selection: "
        ))

        if option == 1:
            print("\nWelcome to the Web Scraping Test!")
            print(
                "Here we will be using BeautifulSoup to CSV files container weekly weather for multiple cities!\n")
            num_process = getNumProcess()
            print("\n")
            for n in num_process:
                time_elapsed = webScraping.main(n)
                print("Test took {} seconds with {} processes".format(
                    time_elapsed, n))

        elif option == 2:
            print("\nWelcome to the Prime Number Calculation Test!")
            print(
                "Here we will calculating the first million prime numbers\n")
            num_process = getNumProcess()
            print("\n")
            for n in num_process:
                time_elapsed = calculatePrime.main(n)
                print("Test took {} seconds with {} processes".format(
                    time_elapsed, n))

        elif option == 3:
            print("\nWelcome to the File Compression Test!")
            print(
                "Here we will be compressing and uncompressing various Disney movie scripts using zlib!\n")
            num_process = getNumProcess()
            print("\n")
            for n in num_process:
                time_elapsed = compression.main(n)
                print("Test took {} seconds with {} processes".format(
                    time_elapsed, n))

        elif option == 4:
            encoding.main()
        elif option == 5:
            print("selected Option 5")
        elif option == 6:
            print("selected Option 6")
        elif option == 7:
            print("Thank you for using our program!")
            sys.exit(0)
        else:
            print("Please enter a valid option")
            continue


def getNumProcess():
    num_process = input(
        "How many processes would you like to test with? You can test multiple values by separating with a space (ie 1 3 5): ").split()
    while(not (str.isdigit(num) for num in num_process)):
        num_process = input("Please enter a valid number(s): ").split()
    return [int(num) for num in num_process]


main()
