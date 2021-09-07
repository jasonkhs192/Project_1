import random

x = random.randint(0, 10000000)
print(x/10000000)

status = True
count = 0
target = 0.1243237

while status == True:
    randNum = random.randint(0, 10000000)
    ranNum = randNum/10000000
    if (ranNum == target):
        print("Found target: {} Count: {}".format(ranNum, count))
        status = False
    else:
        print("Fail: {}".format(ranNum))
        count+=1