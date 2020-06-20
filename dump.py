import requests, json
from urllib.parse import urlencode

from_mate = "http://172.16.0.69:3000"

def get_items(category):
    items = requests.get("%s/api/v1/%s" %(from_mate, category)).json()
    return items

def prepare_params(item, kind):
    params = {}
    for key in item.keys():
        params[kind+"["+key+"]"] = item[key]
    return urlencode(params)

for category in ("users", "drinks"):
    items = get_items(category)
    with open(category+".json", "w") as catfile:
        json.dump(items, catfile)
