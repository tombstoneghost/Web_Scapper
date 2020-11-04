# Imports
import requests as req
from bs4 import BeautifulSoup
import json

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
filtered_list = soup.find_all("a", attr_filter)
print(filtered_list)

# Using CSS selectors
print("\nSelector:\n")
selector = "div.thumb:nth-child(49) > div:nth-child(1) > a:nth-child(1) > img:nth-child(1)"
print(soup.select(selector=selector))

# Sending POST, PUT and PATCH data with modified Headers
print("\nJSON Data:\n")
api_link = 'https://jsonplaceholder.typicode.com/posts'
r = req.get(api_link)
data = json.loads(r.content)
print(data)

print("\nNew JSON Data:\n")
input_data = json.dumps({"title": "test title", "user_id": 5})
headers = {"Content-Type": "application/json"}
r = req.post(api_link, input_data, headers)
data = json.loads(r.content)
print(data)

'''For PUT and PATCH, you can simply use the same code as we have used for POST'''


# Authenticating and maintain connection state through sessions and cookies
print("\nChecking Authentication:\n")
'''This Link might not work, this is just a sample code.'''
link = 'http://testing-ground.scraping.pro/login'

LOGGED_SELECTOR = '#case_login > h3'


def is_logged(html_source):
    global soup
    soup = BeautifulSoup(html_source)
    elements = soup.select(LOGGED_SELECTOR)

    if len(elements) == 1:
        element = elements[0]
        if 'success' in element.get('class', []):
            return True
        else:
            return False
    elif len(elements) > 1:
        raise Exception('Something is wrong with the source')
    else:
        return False


input_data = {"usr": "admin", "pwd": "12345"}
s = req.Session()

r_post = s.post(link + "?mode=login", input_data)
r_get = s.get(link + "?mode=welcome")

print(is_logged(r_post.content))
print(is_logged(r_get.content))
