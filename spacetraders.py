import requests
import re
access_token = ''
# defining the api-endpoint
# l
class setup:
    def createAccount(name,faction):
        link = "https://api.spacetraders.io/v2/register"
        pattern = r'"token":"([^"]+)"' #I used ChatGPT for this; I have a restraining order on regex
        r = requests.post(url=link, data={"symbol": name, "faction": faction})
        match = re.search(pattern, r.text)
        return("Your access key is: " + match[0])

# r = requests.post(url=link, data={"symbol": "213123213",
#     "faction": "COSMIC"})
 
# # extracting response text
# output = r.text
r = requests.get('https://api.spacetraders.io/v2/my/agent',headers ={ 'Authorization':'Bearer {}'.format(access_token)})
print(r.text)



# requests.get()