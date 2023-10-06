import requests
import re
access_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiMjEzMTIzMjEzIiwidmVyc2lvbiI6InYyIiwicmVzZXRfZGF0ZSI6IjIwMjMtMDktMzAiLCJpYXQiOjE2OTY1NDY5MDUsInN1YiI6ImFnZW50LXRva2VuIn0.TnoSysC3TtT5iDXtMMCtwEywn585w4A1eWa95LRfpgsxu15_1gKouLdkw6EyXvYY7av_znwC6Tk4X-zrVCV5xMoVK5auAeJjHDman-ugZLo0my9DAOIl4Dq4oSUKYp1xx9V4vM_d6OHKNLWZJ65fbvrNLdLvA_F7OMCu2B9TxA_5MeYNcEOJ0vMZlNcvGENEUyjHeQ2l1WFa_EPorTXAVSwffQmvgo_X9cNC7F_7qo-JlWkIOIEcqAdVv6C5Cgpq5fJHxss0Nk0vVQXJATOinFyV4ndxEvDzLvsAkKwWCPzIFAGyhflxcezaI_16tDDTWEB1qXKUNgOIUBTNLo26Sw'
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