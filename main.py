import pandas
import requests

from bs4 import BeautifulSoup

oyo_url = "https://www.oyorooms.com/search?location=Kolkata%2C%20West%20Bengal%2C%20India&city=Kolkata&searchType=city&checkin=24%2F04%2F2021&checkout=25%2F04%2F2021&roomConfig%5B%5D=1&guests=1&rooms=1&filters%5Bcity_id%5D=14"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
req = requests.get(oyo_url, headers=headers)
content = req.content
soup = BeautifulSoup(content, "html.parser")
all_hotels = soup.find_all("div", {"class": "oyo-row"})
name = soup.find_all("h3", {"itemprop": "name"})
address = soup.find_all("div", {"itemprop": "address"})
price = soup.find_all("span", {"class": "listingPrice__finalPrice"})
rating = soup.find_all("span", {"class": "hotelRating__ratingSummary"})
hotel_name = []
hotel_address = []
hotel_rating = []
hotel_price = []
for i in name:
    hotel_name.append(i.text)
for i in address:
    hotel_address.append(i.text)
for i in rating:
    hotel_rating.append(i.text)
for i in price:
    hotel_price.append(i.text)
fake = ["","","",""]
scrap_into_csv=[]
scrap_into_csv.append(fake)
scrap_into_csv[0] = ["name", "address", "rating", "price"]
for i in range(len(hotel_name)):
    scrap_into_csv.append(fake)
    scrap_into_csv[i+1]=[hotel_name[i],hotel_address[i],hotel_rating[i],hotel_price[i]]
for i in scrap_into_csv:
    print(i)
data_Frame = pandas.DataFrame(scrap_into_csv)
data_Frame.to_csv("Oyo.csv")
