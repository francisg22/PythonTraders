import requests
import re
access_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiMjEzMTIzMjEzIiwidmVyc2lvbiI6InYyIiwicmVzZXRfZGF0ZSI6IjIwMjMtMDktMzAiLCJpYXQiOjE2OTY1NDY5MDUsInN1YiI6ImFnZW50LXRva2VuIn0.TnoSysC3TtT5iDXtMMCtwEywn585w4A1eWa95LRfpgsxu15_1gKouLdkw6EyXvYY7av_znwC6Tk4X-zrVCV5xMoVK5auAeJjHDman-ugZLo0my9DAOIl4Dq4oSUKYp1xx9V4vM_d6OHKNLWZJ65fbvrNLdLvA_F7OMCu2B9TxA_5MeYNcEOJ0vMZlNcvGENEUyjHeQ2l1WFa_EPorTXAVSwffQmvgo_X9cNC7F_7qo-JlWkIOIEcqAdVv6C5Cgpq5fJHxss0Nk0vVQXJATOinFyV4ndxEvDzLvsAkKwWCPzIFAGyhflxcezaI_16tDDTWEB1qXKUNgOIUBTNLo26Sw'
#I realized publishing this doesnt really matter, its just an account for testing purposes  
class setup:
    def __init__(self,name,faction,key = ''):
        self.name = name
        if(key == ''):
            self.key = setup.createAccount(name,faction)
            if(self.key !=0):
                print('SAVE THIS ACCESS KEY! IF YOU RUN THE PROGRAM AGAIN, YOU WILL NOT BE ABLE TO GET IT BACK')
                print('\n')
            
                print(self.key)
                print('\n'+'ONCE YOU RECORD THIS KEY, INITIALIZE THE OBJECT AGAIN WITH THE KEY')
            else:
                print('Your name is too long (max is 14 characters) or your name has already been taken')
                print('\n')
                print('Please modify your name and try again')
        else:
            self.key = key
    def createAccount(name,faction):
        link = "https://api.spacetraders.io/v2/register"
        pattern = r'"token":"([^"]+)"' #I used ChatGPT for this; I have a restraining order on regex
        r = requests.post(url=link, data={"symbol": name, "faction": faction})
        match = re.search(pattern, r.text)
        if(match == None):
            
            return(0)
        print(match)
        return("Your access key is: " + match[0])
    def viewAgent(self):
        r = requests.get('https://api.spacetraders.io/v2/my/agent',headers ={ 'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
class ship(setup):
    def shipList(self):
        r = requests.get('https://api.spacetraders.io/v2/my/ships', headers ={ 'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def shipLoc(shipNum,sList):
        lst = sList
        return [lst['data'][shipNum]['nav']['systemSymbol'],lst['data'][shipNum]['nav']['waypointSymbol']]
    def locDetails(loc):
        r = requests.get('https://api.spacetraders.io/v2/systems/' + str(loc[0]) +'/waypoints/'+str(loc[1]))
        return r.json()

    
# r = requests.post(url=link, data={"symbol": "213123213",
#     "faction": "COSMIC"})

# # extracting response text
# output = r.text
# r = requests.get('https://api.spacetraders.io/v2/my/agent',headers ={ 'Authorization':'Bearer {}'.format(access_token)})
# print(r.text)



# requests.get()