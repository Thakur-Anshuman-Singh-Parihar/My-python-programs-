import random
your = input("take a number in your mind and press enter")
freind = input("take again the same number for your freind and plus in your number and after all done press enter")
l = []
for i in range (2,100,2):
    l.append(i)
mynum = random.choice(l)
print("and add my number ",mynum)
a = input("press enter if all done")
print("and lastly devide the result by 2 and return the your freind number and press enter after all done")
b = input("press enter if all done")
print("i geuss the remaining value is ",mynum/2)