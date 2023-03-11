class Statistics():
    def __init__(self):
        self.arr = []
    def add(self):
        self.number = int(input())
        self.arr.append(self.number)
    def array(self):
        for x in self.arr:
            print(x,end=' ')
    def greatest(self):
        self.max = self.arr[0]
        for x in self.arr:
            if x > self.max:
                self.max = x
    def smallest(self):
        self.min = self.arr[0]
        for x in self.arr:
            if x < self.min:
                self.min = x
    def arithmetic_mean(self):
        self.sum = 0
        self.len = len(self.arr)
        for x in self.arr:
            self.sum += x
        self.arithmetic = self.sum / self.len
    def median(self):
        self.sort = self.arr
        self.sort.sort()
        if len(self.arr)%2 == 0:
            self.mediana = (self.sort[int(len(self.arr)/2)]+self.sort[int((len(self.arr)/2)-1)])/2
        else:
            self.mediana = self.sort[int(len(self.arr)/2-0.5)]
    def status(self):
        self.greatest()
        self.smallest()
        self.arithmetic_mean()
        self.median()
        print(self.max,self.min,self.arithmetic,self.mediana)
s = Statistics()
s.add()
s.add()
s.add()
s.add()
s.status()
s.status()
        
