try:
    x = float(input('podaj wartosc od 0.0 do 1.0:\n'))
except:
    print('podaj wartosc numeryczna')
if x<0.0 or x>1.0 :
    print('niepoprawna wartosc')
elif x <= 1.0 and x>=0.9 :
    print('5.0')
elif x < 0.9 and x>= 0.8 :
    print('4.5')
elif x < 0.8 and x>= 0.7 :
    print('4.0')
elif x < 0.7 and x>= 0.6 :
    print('3.5')
elif x < 0.6 and x>= 0.5 :
    print('3.0')
elif x < 0.5 and x>= 0.0 :
    print('2.0')
