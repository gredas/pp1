import json
fav = {
    "name":"Onydutek",
    "country":"Poland",
    "year_of_production":2003,
    "rate":8.5,
    "budget":120000
}
x = open('favourite.txt','w')
json.dump(fav,x)