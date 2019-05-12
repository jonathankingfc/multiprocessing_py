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
            "Please select from the following: \n"
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
            webScraping.main()
        elif option == 2:
            print("selected Option 2")
        elif option == 3:
            print("selected Option 3")
        elif option == 4:
            print("selected Option 4")
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


main()
