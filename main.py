import spacetraders
import json
acc = spacetraders.ship('213123213','COSMIC','eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiMjEzMTIzMjEzIiwidmVyc2lvbiI6InYyIiwicmVzZXRfZGF0ZSI6IjIwMjMtMDktMzAiLCJpYXQiOjE2OTY1NDY5MDUsInN1YiI6ImFnZW50LXRva2VuIn0.TnoSysC3TtT5iDXtMMCtwEywn585w4A1eWa95LRfpgsxu15_1gKouLdkw6EyXvYY7av_znwC6Tk4X-zrVCV5xMoVK5auAeJjHDman-ugZLo0my9DAOIl4Dq4oSUKYp1xx9V4vM_d6OHKNLWZJ65fbvrNLdLvA_F7OMCu2B9TxA_5MeYNcEOJ0vMZlNcvGENEUyjHeQ2l1WFa_EPorTXAVSwffQmvgo_X9cNC7F_7qo-JlWkIOIEcqAdVv6C5Cgpq5fJHxss0Nk0vVQXJATOinFyV4ndxEvDzLvsAkKwWCPzIFAGyhflxcezaI_16tDDTWEB1qXKUNgOIUBTNLo26Sw')

print(acc.viewAgent())
shipList = acc.shipList()
with open('shipList.json', 'w') as f:
    json.dump(shipList, f)
print(shipList['data'][0]['nav']['waypointSymbol'])

loc = spacetraders.ship.shipLoc(0,shipList)
print(loc)
print(spacetraders.ship.locDetails(loc))
# print(type(shipList))

# print(shipList['data'][0]['symbol'])
# print(shipList['data'][1]['symbol'])
# key = spacetraders.setup.createAccount('sduifhsduf2','COSMIC')



