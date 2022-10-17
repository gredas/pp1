stawka = float(input('podaj stawke\n'))
godziny = float(input('podaj godziny\n'))
if godziny > 40 :
    wyplata = stawka * godziny * 1.5
else : 
    wyplata = stawka * godziny
print(f'twoja wyplata wynosi {wyplata}')