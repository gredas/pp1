import random
class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
    @staticmethod
    def print_in_row(array):
        string = ''
        for c in array:
            c = str(c)
            string = string + c + ','
        for c in range(len(string)-1):
            print(string[c],end='')
        print()
    @staticmethod
    def same_array(number,value):
        arr = []
        for x in range(number):
            arr.append(value)
        return arr
    @staticmethod
    def range_array(number,fromm,to):
        arr = []
        for x in range(number):
            arr.append(random.randint(fromm,to))
        return arr
    @staticmethod
    def array_range(array,fromm,to):
        count = 0
        for x in array:
            if x <= to and x>=fromm:
                count +=1
        return count
            
my_array = [4,1,8,7,2]
Arrays.print_in_row(my_array)
print(Arrays.same_array(5,2))
print(Arrays.range_array(4,1,5))
print(Arrays.array_range(Arrays.range_array(20,-7,8),-1,1))
