try:
    import requests
    import json

    # Replace with the actual API URL
    api_url = "https://api.restful-api.dev/objects"

    # Send a GET request to the API
    response = requests.get(api_url)

    # Check for successful response
    if response.status_code == 200:
      # Get the data from the response (may vary depending on the API)
      data = response.json()

      # Open a file for writing in write mode ("w")
      with open("data.json", "w") as outfile:
        # Write the data to the file with indentation for readability (optional)
        json.dump(data, outfile, indent=4)
        print("Data written to data.json successfully!")
    else:
      print(f"API request failed with status code: {response.status_code}")
except Exception as e:
    print(e)
