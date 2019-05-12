from multiprocessing import Pool
import bs4 as bs
import random
import requests
import string
import time
import zlib
from random import randint


def main():
    dict = {"Aladdin": "compressionExamples/Aladdin",
            "Beauty and the Beast": "compressionExamples/BeautyandtheBeast",
            "Lion King": "compressionExamples/LionKing",
            "Tarzan": "compressionExamples/Tarzan",
            "The Little Mermaid": "compressionExamples/TheLittleMermaid"}

    num_process = int(input("How many processes would you like to create?"))
    p = Pool(processes=num_process)
    data = p.starmap(compress, list(dict.items()))
    p.close()


def compress(name, path_to_file):
    text = open(path_to_file+".txt", "rb").read()
    with open(path_to_file+".zlib", "wb") as myFile:
        myFile.write(zlib.compress(text))

    print("Compressed {}!".format(name))

    compressedText = open(path_to_file+".zlib", "rb").read()
    decompressed = zlib.decompress(compressedText)

    print("Decompressed {}!".format(name))
