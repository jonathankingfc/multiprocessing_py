import pandas as pd
import requests
from bs4 import BeautifulSoup
import multiprocessing
import time


def main():
    cities = {"new_brunswick": "https://forecast.weather.gov/MapClick.php?lat=40.494770000000074&lon=-74.44383999999997#.XNU9MtNKj6A",
              "los_angeles": "https://forecast.weather.gov/MapClick.php?lat=34.0535&lon=-118.2453#.XNVR8NNKj6A",
              "seattle": "https://forecast.weather.gov/MapClick.php?lat=47.6036&lon=-122.3294#.XNVSG9NKj6A",
              "manhattan": "https://forecast.weather.gov/MapClick.php?lat=40.7145&lon=-74.006",
              "chicago": "https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324"}

    print("Single Process:")
    start = time.time()
    for city, url in cities.items():
        getWeather(city, url)
    end = time.time()
    print("Time Elapsed: {}\n".format(end-start))

    print("Multiple Process:")
    start = time.time()
    process_list = []
    for city, url in cities.items():
        p = multiprocessing.Process(
            target=getWeather, name="{}_thread".format(city), args=(city, url))
        process_list.append(p)
        p.start()

    for p in process_list:
        p.join()
    end = time.time()
    print("Time Elapsed: {}\n".format(end-start))


def getWeather(city, url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    for br in soup.find_all('br'):
        br.replaceWith(" ")

    week = soup.find(id="seven-day-forecast-body")

    items = week.find_all(class_="tombstone-container")

    period_names = [item.find(class_="period-name").get_text()
                    for item in items]
    short_descriptions = [
        item.find(class_="short-desc").get_text() for item in items]
    temperatures = [item.find(class_="temp").get_text() for item in items]

    weather_stuff = pd.DataFrame({
        "period": period_names,
        "short_descriptions": short_descriptions,
        "temperatures": temperatures
    })

    weather_stuff.to_csv(city+".csv")


if __name__ == "__main__":
    print("hello from webScraping")
