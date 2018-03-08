import json, requests
from pprint import pprint
url = 'https://api.foursquare.com/v2/venues/explore'

params = dict(
    client_id='YN0RR2CIPURZ4CAIDQDWETRVQC1ACI5MV3ZWQWYZTGTCOTLJ',
    client_secret='EEGAXWRIXRKOZSVOCUHA5MBDWQX4I4APFOFSDMJ5FHODPULL',
    v='20170801',
    ll='64.126521,-21.817439',
    query='°pizza'
)
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
pprint(data)
for x in data["response"]["groups"]:
    for y in x["items"]:
        if "city" in y["venue"]["location"]:
            if y["venue"]["location"]["city"] == "Reykjavík":
                print(y["venue"]["name"], y["venue"]["location"]["city"])
