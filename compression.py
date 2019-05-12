from multiprocessing import Pool
import bs4 as bs
import random
import requests
import string
import time
import zlib
from random import randint

def compress(randomNum):
    if (randomNum == 1):
        text = open("compressionExamples/Aladdin.txt", "rb").read()
        with open("compressionExamples/compressedAladdin.zlib", "wb") as myFile:
            myFile.write(zlib.compress(text))
        print("Compressed Aladdin!")
        compressedText = open("compressionExamples/compressedAladdin.zlib", "rb").read()
        decompressed = zlib.decompress(compressedText)
        print("Decompressed Aladdin!")
    elif (randomNum == 2):
        text = open("compressionExamples/BeautyandtheBeast.txt", "rb").read()
        with open("compressionExamples/compressedBeautyandtheBeast.zlib", "wb") as myFile:
            myFile.write(zlib.compress(text))
        print("Compressed BeautyandtheBeast!")
        compressedText = open("compressionExamples/compressedBeautyandtheBeast.zlib", "rb").read()
        decompressed = zlib.decompress(compressedText)
        print("Decompressed BeautyandtheBeast!")
    elif (randomNum == 3):
        text = open("compressionExamples/LionKing.txt", "rb").read()
        with open("compressionExamples/compressedLionKing.zlib", "wb") as myFile:
            myFile.write(zlib.compress(text))
        print("Compressed LionKing!")
        compressedText = open("compressionExamples/compressedAladdin.zlib", "rb").read()
        decompressed = zlib.decompress(compressedText)
        print("Decompressed LionKing!")
    elif (randomNum == 4):
        text = open("compressionExamples/Tarzan.txt", "rb").read()
        with open("compressionExamples/compressedTarzan.zlib", "wb") as myFile:
            myFile.write(zlib.compress(text))
        print("Compressed Tarzan!")
        compressedText = open("compressionExamples/compressedTarzan.zlib", "rb").read()
        decompressed = zlib.decompress(compressedText)
        print("Decompressed Tarzan!")
    elif (randomNum == 5):
        text = open("compressionExamples/TheLittleMermaid.txt", "rb").read()
        with open("compressionExamples/compressedTheLittleMermaid.zlib", "wb") as myFile:
            myFile.write(zlib.compress(text))
        print("Compressed TheLittleMermaid!")
        compressedText = open("compressionExamples/compressedTheLittleMermaid.zlib", "rb").read()
        decompressed = zlib.decompress(compressedText)
        print("Decompressed TheLittleMermaid!")

def main():
    how_many = 1
    p = Pool(processes=how_many)
    #parse_us = [random_starting_url() for _ in range(how_many)]
    #data = p.map(get_links, [link for link in parse_us])
    #data = [url for url_list in data for url in url_list]
    data = p.map(compress, [1,2,3,4,5])
    p.close()



if __name__ == '__main__':
    start_time = time.time()
    main()
    print("time taken", time.time() - start_time, "to run")
