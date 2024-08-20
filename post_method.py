try:
    import requests

    requestUrl = "https://api.restful-api.dev/objects"


    response = requests.post(requestUrl, json={"id": 16,"name": "Google Pixel 7 Pro",
                                 "data": {"Capacity": "254 GB",
                                          "Screen size": 7.9}
                                 })

    print (response.status_code)

    print(response.json())
except Exception as e:
    print(e)
