degrees = float(input("Wpisz stopnie celsjusza:\n"))
degreesf = degrees * 9
degreesf = degreesf / 5
degreesf = degreesf + 32
degreesk = degrees + 273.15
print('to tyle stopni kelwina {} oraz tyle stopni farenheita {}' .format(degreesk, degreesf))