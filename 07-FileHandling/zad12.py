x = input("rzecz: ")
y = open('lista.txt','a')
y.write(f'{x}\n')
y.close()