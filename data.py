from bs4 import BeautifulSoup
import requests
import re
from function import regexFunction

# Creating multiple lists to save data
urls = []
oldNameList = []

nameList = []
priceList = []
subModelList = []
distanceList = []
cityList = []
useTypeList = []
yearList = []
vehicleOverview = []
newPriceList = []


# Input url
mainUrl = 'https://www.truecar.com/used-cars-for-sale/listings/?page=10'  # Input url

reqs = requests.get(mainUrl)  # grab data from a data source

soup = BeautifulSoup(reqs.text, 'html.parser')  # Pulling data out of HTML

# Extracting existing links related to cars
for link in soup.find_all('a', attrs={"class": "linkable vehicle-card-overlay order-2"}):
    new_url = link.get('href')
    urls.append(f"https://www.truecar.com{link.get('href')}")

# Extracting the name of the cars
names = soup.find_all('span', attrs={"class": "truncate"})
for name in names:
    oldNameList.append(name.text)
nameList = oldNameList[::2]

# Extracting the year of the car
yearOfConstruction = soup.find_all('span', attrs={"class", "vehicle-card-year text-xs"})
for year in yearOfConstruction:
    yearList.append(year.text)

# Extracting the price of the cars
prices = soup.find_all('span', attrs={"data-test": "vehicleListingPriceAmount"})
for price in prices:
    priceList.append(price.text)
for i in priceList:  # Convert price str to float and add to new list
    r, n = re.subn(',', '', i)
    newPriceList.append(float(r[1:]))

# Extracting the distance traveled
distances = soup.find_all('div', attrs={"class": "truncate text-xs", "data-test": "vehicleMileage"})
for distance in distances:
    distanceList.append(distance.text)


info = soup.find_all('div', attrs={"class": "vehicle-card-location mt-1 text-xs", "data-test": "vehicleCardCondition"})
for i in info:
    useTypeList.append(i.text)

# Extraction of the city of cars
cities = soup.find_all('div', attrs={"class": "vehicle-card-location mt-1 text-xs", "data-test": "vehicleCardLocation"})
for city in cities:
    cityList.append(city.text)

# Extraction of the color of cars


# Extraction of the sub Model of cars
for i in urls:
    reqs = requests.get(i)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    subModel = soup.find('span', attrs={"class": "mr-2 pr-2 border-r border-r-[#999999]"})
    subModelList.append(subModel.text)

# Extraction the Vehicle Overview
for i in urls:
    req = requests.get(i)
    soup = BeautifulSoup(req.text, "html.parser")
    fuel = soup.find_all('div', attrs={"class": "mb-3 lg:mb-4 col-12 col-lg-6"})
    for f in fuel:
        vehicleOverview.append(f.text)


# Extraction the fuel type of cars
fuelTypeList = regexFunction("Fuel .*", vehicleOverview)  # Extraction the fuel type of cars

# Extraction the transmission of cars
transmissionType = regexFunction(".*Transmission", vehicleOverview)  # Extraction the Transmission type of cars

# Extraction the wheel drive type of cars
wheelDriveType = regexFunction(".*WD", vehicleOverview)  # Extraction wheel drive type

# Extraction the engine type of cars
engineType = regexFunction(".*L .*", vehicleOverview)  # Extraction the engine type of cars

# Extraction the exterior color of cars
exteriorColor = regexFunction("Exterior.*", vehicleOverview)
# Extraction the interior color of cars
interiorColor = regexFunction("Interior.*", vehicleOverview)
