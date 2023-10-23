import time
gameStart = input("Want to play MadLibs? y/n")
if gameStart == "y":
    print("Let's Play!")
elif gameStart == "n":
    print("you opened this, so i feel like you're trolling... Let's Play!")
else:
    print(f"{gameStart}? I'll take that as a yes. Let's Play!")
land = input("Give me a city, country, or any other place like that")
name1 = input("Okay, now give me a man's name")
place = input("Great, give me a store or a resteraunt or anywhere where you buy things")
obj = input("Now give me an object")
name2 = input("Provide me with a girl's name")
subject = input("Give me a subject to talk about")
food = input("Give me a food")
anything = input("Now give me ANYTHING!")
doingSomething = input("Give me something something is doing")
superhero = input("Provide me with a superhero name")
foodPlace = input("Lastly, give me a food place")
print("Great! Let me just look over your answers for a moment...")
time.sleep(2)
print("Finished! Enjoy your story!")
time.sleep(.5)
print("")
print(f"{name1} walks to {place}")
chars = f'One day in the land of {land}, a man named {name1} walked to a {place} to get some {obj}s. {name1} met his friend {name2} at the {place}. They talked about {subject} and ate {food}. Suddenly, a giant {anything} appeared and started {doingSomething}. Fortunitly, the superhero {superhero} arrived and slayed the beast! {name1}, {name2}, and {superhero} all got food at {foodPlace} and went home.'
loop = range(1, len(chars) + 1)

for idx in loop:
    print(chars[:idx], end='\r') # <-- end with carriage return
    time.sleep(.1)