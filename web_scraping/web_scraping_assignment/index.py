import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.magicbricks.com/property-for-sale/residential-real-estate?&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Noida')
soup = BeautifulSoup(response.text, 'html.parser')


print(soup)

