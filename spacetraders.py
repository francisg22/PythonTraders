import requests
import re
import json
access_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiMjEzMTIzMjEzIiwidmVyc2lvbiI6InYyIiwicmVzZXRfZGF0ZSI6IjIwMjMtMDktMzAiLCJpYXQiOjE2OTY1NDY5MDUsInN1YiI6ImFnZW50LXRva2VuIn0.TnoSysC3TtT5iDXtMMCtwEywn585w4A1eWa95LRfpgsxu15_1gKouLdkw6EyXvYY7av_znwC6Tk4X-zrVCV5xMoVK5auAeJjHDman-ugZLo0my9DAOIl4Dq4oSUKYp1xx9V4vM_d6OHKNLWZJ65fbvrNLdLvA_F7OMCu2B9TxA_5MeYNcEOJ0vMZlNcvGENEUyjHeQ2l1WFa_EPorTXAVSwffQmvgo_X9cNC7F_7qo-JlWkIOIEcqAdVv6C5Cgpq5fJHxss0Nk0vVQXJATOinFyV4ndxEvDzLvsAkKwWCPzIFAGyhflxcezaI_16tDDTWEB1qXKUNgOIUBTNLo26Sw'
#I realized publishing this doesnt really matter, its just an account for testing purposes  
#https://spacetraders.stoplight.io/docs/spacetraders/403855e2e99ad-purchase-ship
def toFile(text, filename):
    with open(filename + '.json', 'w') as f:
        json.dump(text, f)
def jsonToString(details):
    str = json.dumps(details, indent=4, separators=(',', ': '), sort_keys=True)
    return str
    # if type == 'market':
    #     for el in details['data'].keys():
    #         if el == 'symbol':
    #             continue
    #         for i in details['data'][el]:
    #             print(i)
    #             print('\n')
    # if type == 'sys':
        

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
    # def shipLoc(shipNum,sList):
    #     lst = sList
    #     return [lst['data'][shipNum]['nav']['systemSymbol'],lst['data'][shipNum]['nav']['waypointSymbol']]
    def buyShip(self,shipname, loc):
        link = 'https://api.spacetraders.io/v2/my/ship'
        r = requests.post(link, data={"shipType": shipname, "waypointSymbol": loc}, headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def getShip(self, name):
        r = requests.get('https://api.spacetraders.io/v2/my/ships/'+name, headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def getCargo(self, name):
        r = requests.get('https://api.spacetraders.io/v2/my/ships/'+name+'/cargo', headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def orbit(self,name):
        r = requests.post('https://api.spacetraders.io/v2/my/ships/'+name+'/orbit', headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def refine(self,name,mats):
        r = requests.post('https://api.spacetraders.io/v2/my/ships/'+name+'/refine', data={'produce':mats}, headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def chart(self,name):
        r = requests.post('https://api.spacetraders.io/v2/my/ships/'+name+'/chart', headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def getCooldown(self,name):
        r = requests.get('https://api.spacetraders.io/v2/my/ships/'+name+'/cooldown', headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.text
    def dock(self,name):
        r = requests.post('https://api.spacetraders.io/v2/my/ships/'+name+'/dock', headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def survey(self,name):
        r = requests.post('https://api.spacetraders.io/v2/my/ships/'+name+'/survey', headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def extractResource(self,name,survey):
        r = requests.post('https://api.spacetraders.io/v2/my/ships/'+name+'/extract', data = {survey}, headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def extractResource(self,name,survey):
        r = requests.post('https://api.spacetraders.io/v2/my/ships/'+name+'/extract/survey', data = {survey}, headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def jettison(self,name,cargo):
        r = requests.post('https://api.spacetraders.io/v2/my/ships/'+name+'/jettison', data = {cargo}, headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def jump(self,name,sys):
        r = requests.post('https://api.spacetraders.io/v2/my/ships/'+name+'/jump', data = {"systemSymbol": sys}, headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def navigate(self,name,loc):
        r = requests.post('https://api.spacetraders.io/v2/my/ships/'+name+'/navigate', data = {"waypointSymbol": loc}, headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def shipNav(self, name, navType):
        r = requests.patch('https://api.spacetraders.io/v2/my/ships/'+name+'/nav', data = {"flightMode": navType}, headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def getNav(self,name):
        r = requests.get('https://api.spacetraders.io/v2/my/ships/'+name+'/nav', headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def warp(self, name, loc):
        r = requests.post('https://api.spacetraders.io/v2/my/ships/'+name+'/warp', data = {"waypointSymbol": loc}, headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def sellCargo(self,name, cargo, amount):
        r = requests.post('https://api.spacetraders.io/v2/my/ships/'+name+'/sell', data = {"symbol": cargo, "units": amount}, headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def scanSystems(self,name):
        r = requests.post('https://api.spacetraders.io/v2/my/ships/'+name+'/scan/systems', headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def scanWaypoints(self,name):
        r = requests.post('https://api.spacetraders.io/v2/my/ships/'+name+'/scan/waypoints', headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def scanShips(self,name):
        r = requests.post('https://api.spacetraders.io/v2/my/ships/'+name+'/scan/ships', headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def refuel(self,name, amount):
        r = requests.post('https://api.spacetraders.io/v2/my/ships/'+name+'/refuel', data = {"units": amount}, headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def buyCargo(self,name, cargo, amount):
        r = requests.post('https://api.spacetraders.io/v2/my/ships/'+name+'/purchase', data = {"symbol": cargo, "units": amount}, headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def tranferCargo(self,name, ship, cargo, amount):
        r = requests.post('https://api.spacetraders.io/v2/my/ships/'+name+'/transfer', data = {"tradeSymbol": cargo, "units": amount,"shipSymbol": ship}, headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def negotiate(self,name):
        r = requests.post('https://api.spacetraders.io/v2/my/ships/'+name+'/negotiate/contract', headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def getMounts(self,name):
        r = requests.get('https://api.spacetraders.io/v2/my/ships/'+name+'/mounts', headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def installMounts(self,name,mount):
        r = requests.post('https://api.spacetraders.io/v2/my/ships/'+name+'/mounts/install',data = {"symbol": mount}, headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def removeMounts(self,name,mount):
        r = requests.post('https://api.spacetraders.io/v2/my/ships/'+name+'/mounts/remove',data = {"symbol": mount}, headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    
class contracts(ship):
    def listContracts(self):
        r = requests.get('https://api.spacetraders.io/v2/my/contracts', headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def getConract(self,contract):
        r = requests.get('https://api.spacetraders.io/v2/my/contracts/' + contract, headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def acceptContract(self,contract):
        r = requests.post('https://api.spacetraders.io/v2/my/contracts/' + contract + '/accept', headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def deliverCargo(self,contract,ship,cargo,amount):
        r = requests.post('https://api.spacetraders.io/v2/my/contracts/' + contract + '/deliver', data = {"shipSymbol": ship, "tradeSymbol": cargo, "units": amount}, headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def fufillContract(self,contract):
        r = requests.post('https://api.spacetraders.io/v2/my/contracts/' + contract + '/fulfill', headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
class account(contracts):
    def listFactions():
        r = requests.get('https://api.spacetraders.io/v2/factions')
        return r.json()
    def getFaction(self,faction):
        r = requests.get('https://api.spacetraders.io/v2/factions/'+ faction, headers = {'Authorization':'Bearer {}'.format(self.key)})
        return r.json()
    def getPubAgent(agent):
        r = requests.get('https://api.spacetraders.io/v2/agents/' + agent)
        return r.json()
    def listAgents():
        r = requests.get('https://api.spacetraders.io/v2/agents')
        return r.json()
    


    
    
    
    
    
    
    
    
    
    
    
class systems:
    #if readme is used - remember to put loc is [system,waypoint]
    def locDetails(loc):
        r = requests.get('https://api.spacetraders.io/v2/systems/' + str(loc[0]) +'/waypoints/'+str(loc[1]))
        return r.json()
    def systemList():
        r = requests.get('https://api.spacetraders.io/v2/systems')
        return r.json()
    def sysDetails(system):
        r = requests.get('https://api.spacetraders.io/v2/systems/' + system)
        return r.json()
    def sysWaypoints(system):
        r = requests.get('https://api.spacetraders.io/v2/systems/' + system + '/waypoints')
        return r.json()
    def marketDetails(loc):
        r = requests.get('https://api.spacetraders.io/v2/systems/' + str(loc[0]) +'/waypoints/'+ str(loc[1]) + '/market') 
        return r.json()
    def shipyardDetails(loc):
        r = requests.get('https://api.spacetraders.io/v2/systems/' + str(loc[0]) +'/waypoints/'+ str(loc[1]) + '/shipyard')
        return r.json()
    def jumpGateDetails(loc):
        r = requests.get('https://api.spacetraders.io/v2/systems/' + str(loc[0]) +'/waypoints/'+ str(loc[1]) + '/jump-gate')
        return r.json()
    
    
               
# r = requests.post(url=link, data={"symbol": "213123213",
#     "faction": "COSMIC"})

# # extracting response text
# output = r.text
# r = requests.get('https://api.spacetraders.io/v2/my/agent',headers ={ 'Authorization':'Bearer {}'.format(access_token)})
# print(r.text)



# requests.get()