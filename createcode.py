import random

a=[]
num=0

while (len(a)<100000):
    num = random.randrange(00000,99999)
    if num in a:
        print("")
    else:
        print (num)
        a.insert(num, num)