# Imports
import requests as req
from bs4 import BeautifulSoup

# Target URL
URL = "https://pt.wikipedia.org/wiki/Ariquemes"

# Get Page Content
r = req.get(URL)
soup = BeautifulSoup(r.content, features="html.parser")

# Printing Data
print("Web Page:\n")
print(soup.prettify())

# Printing all Tables
print("\nTables:\n")
tables = soup.find_all("table")
print(tables)

# Finding all Lists
print("\nLists:\n")
lists = soup.find_all("li")
print(len(lists))

# Finding Children of some element
print("\nList Children:\n")
childs = list(lists[3].children)
print(childs)

# Finding Links
print("\nLinks:\n")
links = soup.find_all("a")
print(len(links))

# Applying Attribute Filter
print("\nFiltered Link List:\n")
attr_filter = {"class": "mw-jump-link", "href": "#mw-head"}
filtered_list = soup.find_all(attr_filter)
print(filtered_list)
