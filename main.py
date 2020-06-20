import requests
from urllib.parse import urlencode

from_mate = "http://172.16.0.69:3000"
to_mate = "http://mete.cloud.cccfr"

def get_items(category):
    items = requests.get("%s/api/v1/%s" %(from_mate, category)).json()
    return items

def set_item(item, category):
    params = prepare_params(item, category.strip("s"))
    print(params)
    print(requests.post("%s/api/v1/%s" %(to_mate, category), params=params, headers={'Content-Type': 'application/json'}))

def prepare_params(item, kind):
    params = {}
    for key in item.keys():
        params[kind+"["+key+"]"] = item[key]
    return urlencode(params)

for category in ("users", "drinks"):
    items = get_items(category)
    for item in items:
        set_item(item, category)
