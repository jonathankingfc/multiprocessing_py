from multiprocessing import Pool
import bs4 as bs
import random
import requests
import string
import time
import zlib
from random import randint


def compress(name, path_to_file):
    text = open(path_to_file+".txt", "rb").read()
    with open(path_to_file+".zlib", "wb") as myFile:
        myFile.write(zlib.compress(text))

    print("Compressed {}!".format(name))

    compressedText = open(path_to_file+".zlib", "rb").read()
    decompressed = zlib.decompress(compressedText)

    print("Decompressed {}!".format(name))


def main():
    dict = {"Aladdin": "compressionExamples/Aladdin",
            "Beauty and the Beast": "compressionExamples/BeautyandtheBeast",
            "Lion King": "compressionExamples/LionKing",
            "Tarzan": "compressionExamples/Tarzan",
            "The Little Mermaid": "compressionExamples/TheLittleMermaid"}
    how_many = 100
    p = Pool(processes=how_many)
    # print(list(dict.items()))
    data = p.starmap(compress, list(dict.items()))
    p.close()


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time taken", time.time() - start_time, "to run")
