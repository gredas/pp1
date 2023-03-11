import json
f1 = open('euro.json','r')
f2 = json.load(f1)
print(f1)
print(f2["ExchangeRatesSeries"]["Rates"]['rate'])
