import random
randomNumber = random.randint(1, 1000)
while True:
    numberUser = int(input())
    if numberUser == randomNumber:
        print("You crazy!!! WOW")
        break
    elif numberUser > 1000:
        print("You tutu?")
    else:
        print("nope")