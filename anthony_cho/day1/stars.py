# part 1
def draw_stars(list):
    for num in list:
        print(num*"*")


draw_stars([1,2,3,4,5])

#part 2
def draw_stars2(list):
    for thing in list:
        if type(thing) is int:
            print(thing * "*")
        else:
            print(len(thing) * thing[:1])

draw_stars2([1,2,3,4,5,"thing"])
