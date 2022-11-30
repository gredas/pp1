import random
def rand_element(n):
    x = random.randint(0,len(n)-1)
    return n[x]
print(rand_element([1,2,3,4,5,6,7,8]))