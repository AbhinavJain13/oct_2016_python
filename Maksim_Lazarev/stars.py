# # Part 1
# def draw_stars(x):
#     for i in x:
#         str=""
#         for r in range(0,i):
#             str+="*"
#         print (str)
# x = [4,6,1,3,5,7,25]
# draw_stars(x)

# Part 2
def draw_stars(x):
    for i in x:
        str=""
        try:
            int(i)
            for r in range(0,i):
                str+="*"
        except ValueError:
            for r in range(0,len(i)):
                str+= (i[0]).lower()
        print (str)
x = [4,"Tom",1,"Michael",5,7,"Jimmy Smith"]
draw_stars(x)
