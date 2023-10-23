import random

adj = ["dumb", "happy", "annoying", "strange", "funny", "upside-down", "insane", "dead inside"]
noun = ["orange", "cow", "moon", "swift", "goe giden", "stormtrooper at 23:41 - 23:50 in star wars episode 5", "tree", "mr beast"]
noun2 = ["walter white", "jesse from breaking bad", "jesse from minecraft story mode", "jesse from toy story", "pewdiepie", "rick astley", "obama"]
noun3 = ["peter pan", "peter quill", "peter griffin", "pete from mickey mouse", "pete the cat", "peter parker", "peter pettigrew", "peter rabbit", "peter from home alone"]
verb = ["walked", "ran", "swam", "flew", "teleported", "sprinted", "crawled", "BLJ'd"]

def r(x):
    return random.choice(x)

print("the", r(adj), r(noun), r(verb), "to the", r(adj), r(noun2), "'s house with the", r(adj), r(noun3))
print("the", r(adj), r(noun), r(verb), "to the", r(adj), r(noun2), "'s house with the", r(adj), r(noun3))
print("the", r(adj), r(noun), r(verb), "to the", r(adj), r(noun2), "'s house with the", r(adj), r(noun3))
print("the", r(adj), r(noun), r(verb), "to the", r(adj), r(noun2), "'s house with the", r(adj), r(noun3))
print("the", r(adj), r(noun), r(verb), "to the", r(adj), r(noun2), "'s house with the", r(adj), r(noun3))
