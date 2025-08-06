import requests
from sys import argv
from bs4 import BeautifulSoup

url = ('https://coincap.io/')

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
span = soup.find_all('span', class_="Numeral__Container-sc-18j7kzw-0jbOTGsnumeral")
print(span)
