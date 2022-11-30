tab = [1,2,3,4,5]
print(tab)

tab[-1] = tab[-1] + 4
print(tab)
tab[len(tab)//2] = tab[len(tab)//2] *2
print(tab)
for x in range(0,len(tab)):
    tab[x] = tab[x] + 3
print(tab)
