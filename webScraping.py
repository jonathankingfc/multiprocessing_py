import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get(
    "https://forecast.weather.gov/MapClick.php?lat=40.494770000000074&lon=-74.44383999999997#.XNU9MtNKj6A")
soup = BeautifulSoup(page.content, "html.parser")

for br in soup.find_all('br'):
    br.replaceWith(" ")

week = soup.find(id="seven-day-forecast-body")

items = week.find_all(class_="tombstone-container")


period_names = [item.find(class_="period-name").get_text() for item in items]
short_descriptions = [
    item.find(class_="short-desc").get_text() for item in items]
temperatures = [item.find(class_="temp").get_text() for item in items]

weather_stuff = pd.DataFrame({
    "period": period_names,
    "short_descriptions": short_descriptions,
    "temperatures": temperatures
})

print(weather_stuff)
