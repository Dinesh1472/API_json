try:
    import requests
    import json

    headers = {"content-type": "application/json"}
    payload = json.dumps({ "name": "Apple AirPods",
                           "data": { "color": "white",
                                     "generation": "3rd", "price": 135}})
    requestUrl = "https://api.restful-api.dev/objects/ff808181916d7dce01916e07d61e012d"
    r = requests.put(requestUrl, data=payload, headers=headers)

    print(r.content)

except Exception as e:
    print(e)
