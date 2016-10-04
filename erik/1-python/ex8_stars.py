
data=[1,2,3,4,5,6]
def fullOfStars(ary):
    for value in ary:
        print "*"*value
fullOfStars(data)

data=["Meg Myers",25,"Madonna",44,"Sky Ferriera"]
def fullOfStars2(ary):
    for idx,value in enumerate(ary):
        try:
            print "*"*value
        except:
            print value[0]*len(value)
fullOfStars2(data)

# - - - - - - - - - - - - - - - - - - -

one = '6'
vals = dict(one=1, two=2)
print vals
print vals['one']
# {'two': 2, 'one': 1}

vals2 = dict(testing=1, testingtwo=2)
print vals2

firstday = "Sun"
weekend = { firstday: "Sunday", "Mon": "Monday" }
print weekend

d = { i: object() for i in range(4) }
print d

capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["dkd"] = ["here","there","nowhere"]
print capitals
print str(capitals)
print capitals.items()
# [('dkd', ['here', 'there', 'nowhere']), ('svk', 'Bratislava')]
