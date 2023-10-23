import random

plrwins = 0
comwins = 0
tie = 0
commoveL = ["r", "p", "s"]
commove = "n"

gameStart = input("Want to play RPS 2? y/n")
if gameStart == "y":
    print("Let's Play!")
elif gameStart == "n":
    print("you opened this, so i feel like you're trolling... Let's Play!")
else:
    print(f"{gameStart}? I'll take that as a yes. Let's Play!")
while True:
    plrmove = input("Choose your move! Options: r, p, s, tally, exit")
    commove = random.choice(commoveL)
    if plrmove == "rock":
        print("eh? rocks dont exist here!")
    elif plrmove == "paper":
        print("bro the trees are gone")
    elif plrmove == "scissors":
        print("um actually we use nuclear bombs to cut stuff now")
    #moves
    elif (plrmove == "rizz") or (plrmove == "r"):
        if commove == "r":
            print("we both are RIZZICAL! (tie)")
            tie += 1
        elif commove == "p":
            print("L no rizz (i win)")
            comwins += 1
        elif commove == "s":
            print("L have rizz (you win)")
            plrwins += 1
        else:
            print("something broke uh oh")
    elif (plrmove == "pancake") or (plrmove == "p"):
        if commove == "r":
            print("im gonna make a pancake out of your di- (you win)")
            plrwins += 1
        elif commove == "p":
            print("why are they called pancakes? are they pansexual cakes or something...? (tie)")
            tie += 1
        elif commove == "s":
            print("protip: always add chocolate chips (i win)")
            comwins += 1
        else:
            print("something broke uh oh")
    elif (plrmove == "scott") or (plrmove == "s"):
        if commove == "r":
            print("ready for a ten hour long lecture after talking to a brick wall? (i win)")
            comwins += 1
        elif commove == "p":
            print("u brick wall (you win)")
            plrwins += 1
        elif commove == "s":
            print("scott will be notified MWHAHAHAHHAHSDGSHAFBHAS (tie)")
            tie += 1
        else:
            print("something broke uh oh")
    elif plrmove == "tally":
        print(f"wins: {plrwins}")
        print(f"losses: {comwins}")
        print(f"ties: {tie}")
    elif plrmove == "exit":
        exit()
    else:
        print("not an option")