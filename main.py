import spacetraders
#Failed to parse token. Token reset_date does not match the server. 
#Server resets happen on a weekly to bi-weekly frequency during alpha. After a reset, you should re-register your agent. 
acc = spacetraders.contracts('213123213','COSMIC','eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiMjEzMTIzMjEzIiwidmVyc2lvbiI6InYyIiwicmVzZXRfZGF0ZSI6IjIwMjMtMTAtMTQiLCJpYXQiOjE2OTc1Njc5NzYsInN1YiI6ImFnZW50LXRva2VuIn0.V31N6vzGQx8yD5iyoqmQPmNjEyh6st55zDrJGeB1Rgu2PzmTZH3XMkaHHIIgpKVU89QTxJvMYwqOJfsDNHunREvhC_1fAiKQsCWIlos-O3vq6N3GhKn_snVMw8SSMZnJDgjhdMZjjNxbAP1S5xmWHrmk_6Udil7LdNRiyqXp-8qghwKGfgCo6oBtPk1DneEd7y7t9WkwjHyS5d1XLW5krRRYcOir2jfwGglN6hvOAnVOgZYisZ8TTBEN986dSvnMbP21FOqiks6MTleXtp7zWu4EecOmGAHVdrrMzJD9UtOI8w73w4UzPfwFp1f7jViptC7hGbo1nB_HrHZrvpMCwA')

print(acc.viewAgent())
shipList = acc.shipList()
spacetraders.toFile(shipList,'shipList')
# print(shipList['data'][0]['nav']['waypointSymbol'])

loc = spacetraders.ship.shipLoc(0,shipList)
# # print(loc)
# #print(spacetraders.systems.locDetails(loc))
sys = spacetraders.systems.locDetails(loc)
# # print(spacetraders.systems.marketDetails(loc))
# # print(type(shipList))
# print(loc)
# # details = spacetraders.systems.marketDetails(loc)
# # print(len(details['data']))

#print(spacetraders.jsonToString(sys))
print(spacetraders.jsonToString(acc.getConracts()))
# print(shipList['data'][0]['symbol'])
# print(shipList['data'][1]['symbol'])
# key = spacetraders.setup.createAccount('sduifhsduf2','COSMIC')



