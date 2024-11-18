import random

a=[]
f = open("passlist.txt", "a")
num=0

while (len(a)<99999):
    num = random.randrange(00000,99999)
    if num in a:
        print("")
    else:
        print (num)
        a.insert(num, num)
        b=str(num)
        c=(b)
        d=str(c)
        f.write(c)
        f.write("\n")