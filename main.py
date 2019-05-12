import webScraping
import calculatePrime
import compression
import encoding
import argparse
import sys
import mysort
import graphs


def main():
    print("\n================================================================================\nWelcome to our program! We will be testing the multiprocessing module on various workloads.")
    while(True):
        option = int(input(
            "\nPlease select from the following: \n"
            "1. Web Scraping\n"
            "2. Calculating Primes\n"
            "3. Compressing Text Files\n"
            "4. Encoding Image Files\n"
            "5. Sorting Integer Lists\n"
            "6. Show Graph\n"
            "7. Clean Workspace\n"
            "8. Quit Program\n"
            "Selection: "
        ))
        while(not (str.isdigit(option))):
			option = input("Please enter a valid number: ")

		option = int(option)
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
            print("\nWelcome to the Encoding Test!")
            print(
                "Here we will be pulling images from Reddit and encoding them with unidecode!\n")
            num_process = getNumProcess()
            print("\n")
            for n in num_process:
                time_elapsed = encoding.main(n)
                print("Test took {} seconds with {} processes".format(
                    time_elapsed, n))

        elif option == 5:
            print("\nWelcome to the Sorting Test!")
            print(
                "Here we will be \n")
            num_process = getNumProcess()
            print("\n")
            for n in num_process:
                time_elapsed = mysort.main(n)
                print("Test took {} seconds with {} processes".format(
                    time_elapsed, n))
        elif option == 6:
            print(
                "We will export the graph as a png in the current directoy. This may take some time!")
            graphs.lineGraph()
            webScraping.clean()
            calculatePrime.clean()
            compression.clean()
        elif option == 7:
            webScraping.clean()
            calculatePrime.clean()
            compression.clean()
            print("Workspace has been cleaned!")
        elif option == 8:
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
