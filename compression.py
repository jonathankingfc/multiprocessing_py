from multiprocessing import Pool
import bs4 as bs
import random
import requests
import string
import time
import zlib
from random import randint
import shutil
import os


def main(num_process):
    movies = {"Aladdin": "testFiles/Aladdin",
              "BeautyandtheBeast": "testFiles/BeautyandtheBeast",
              "LionKing": "testFiles/LionKing",
              "Tarzan": "testFiles/Tarzan",
              "TheLittleMermaid": "testFiles/TheLittleMermaid"}

    clean()
    os.mkdir("compressedFiles")
    os.mkdir("uncompressedFiles")

    start = time.time()
    p = Pool(processes=num_process)
    p.starmap(compress, list(movies.items()))
    p.close()
    p.join()

    end = time.time()
    duration = end - start

    return duration


def compress(name, path_to_file):

    text = open(path_to_file+".txt", "rb").read()
    with open("compressedFiles/"+name+".zlib", "wb") as myFile:
        myFile.write(zlib.compress(text))

    compressedText = open("compressedFiles/"+name+".zlib", "rb").read()

    with open("uncompressedFiles/"+name+".txt", "wb") as myFile:
        myFile.write(zlib.decompress(compressedText))


def clean():
    if(os.path.isdir(os.getcwd()+"/compressedFiles")):
        shutil.rmtree(os.getcwd()+"/compressedFiles")
    if(os.path.isdir(os.getcwd()+"/uncompressedFiles")):
        shutil.rmtree(os.getcwd()+"/uncompressedFiles")
