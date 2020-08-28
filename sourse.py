import random
randomNumber = random.randint(1, 10)
x = 1
while True:
    numberUser = int(input())
    if numberUser == randomNumber:
        print("You crazy!!! WOW")
        break
    elif numberUser > 10:
        print("You tutu?")
    else:
        x += 1
        print("nope")
print(randomNumber)
print(x)
