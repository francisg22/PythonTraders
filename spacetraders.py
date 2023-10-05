import requests
 
# defining the api-endpoint
link = "https://api.spacetraders.io/v2/register"
 

r = requests.post(url=link, data={"symbol": "213123213",
    "faction": "COSMIC"})
 
# extracting response text
output = r.text
print(output)