from multiprocessing import Pool
import bs4 as bs
import random
import requests
import string
import time
import zlib
import json
import time
import os
import unidecode
import base64
from random import randint


def main(num_process):
    urls = get_headlines()

    start = time.time()
    p = Pool(processes=num_process)
    p.map(getEncoded, urls)
    p.close()
    p.join()
    end = time.time()

    duration = end - start

    return duration


def get_headlines():
    user_pass_dict = {'user':  'PrinProgFinalProject',
                      'passwd': 'ilovepython',
                      'api_type': 'json'}
    sess = requests.Session()
    sess.headers.update({'User-Agent': 'Image Testing: PrinProgFinalProject'})
    sess.post('https://www.reddit.com/api/login', data=user_pass_dict)
    time.sleep(1)
    url = 'https://www.reddit.com/r/pic/.json?limit=10'
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))
    titles = [unidecode.unidecode(listing['data']['url'])
              for listing in data['data']['children']]
    urls = []
    urls.append(titles)
    return titles


def getEncoded(url):
    encoded = base64.b64encode(requests.get(url).content)
    return encoded
