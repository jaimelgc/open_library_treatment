import requests
from urllib.request import urlopen
import json


url = "https://openlibrary.org/search.json?q=king"
headers = {
    "User-Agent": "OLTest/0.1 (jaimelg016@gmail.com)"
}
response = requests.get(url, headers=headers)

with open('data_raw/author_search,json', 'w') as f:
    data = response.json()
    json.dump(data, f, ensure_ascii=False, indent=2)
