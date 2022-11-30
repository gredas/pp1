person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }
print(person)
print(person['name'])
print(person['hobby'])
person['surname'] = 'Nowak'
person['hobby'].append('bicycle')
person['phone']['work'] = '3131313213'
print(person)