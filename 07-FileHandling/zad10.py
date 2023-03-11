name = 'Bartlomiej\n'
surname = 'Greda\n'
uni = 'UEK\n'
field_of_study = 'Aplied Informatic\n'
f = open('me.txt','w')
f.write(name)
f.write(surname)
f.write(uni)
f.write(field_of_study)
f.close()