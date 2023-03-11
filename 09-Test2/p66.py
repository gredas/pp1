# Create a function f(age, course, average) that, for the test.json file, 
# returns the number of students who have at least the given number of years and 
# have at least the given grade average in the given course. Example:
# f(21, "statistics", 4) => compare results with other students

import json
def f(age,course,average):    
    iloscosob = 0
    with open('test.json', 'r') as file:
        data = json.load(file)
        for person in data:
            if person['age'] >= age:
                for element in person['studies']['courses']:
                    if element['name'] == course:
                        suma = 0
                        ilosc = 0
                        for grade in element['grades']:
                            suma += grade
                            ilosc += 1
                        if suma/ilosc >= average:
                            iloscosob += 1
                            print(person["name"])
    return iloscosob                    
print(f(21,"statistics",4))