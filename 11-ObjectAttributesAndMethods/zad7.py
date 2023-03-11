class Student():
    university = 'UEK'
    number = 100000
    def __init__(self,name,surname,fos):
        self.name = name
        self.surname = surname
        self.fos = fos
        self.album = self.number
        Student.number += 1
a=Student('b','g','inf')
b=Student('v','s','ada')
print(a.album,b.album)

