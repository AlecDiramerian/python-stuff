import random
while True:
    num = random.randint(1, 1000000000000)
    print(num)
while True:
    guess = int(input("i chose a number between 1 and 1000000000000, guess it"))
    if guess < num:
        print("higher")
    elif guess > num:
        print("lower")
    else:
        print("ladies and gentlemen... you gottem")
        break