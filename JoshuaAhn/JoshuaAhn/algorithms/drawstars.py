# # x = [4,6,1,3,5,7,25]
# def draw_stars(arr):
#    for i in range (len(arr)):
#        arr[i] *= "*"
#        print arr[i]
# draw_stars(x)

a= [4, "tom", 1, "micheal", 5, 7, "Jimmy Smith"]
def draw_stars(arr):
    for i in range(len(arr)):
        if   arr[i] % 1 == 0:
            arr[i] *="*"
            print arr[i]
        else:
            print arr[i] * len(arr[0][0])
draw_stars(a)



# x = ["name","another"]
#
# print x[1]
# print x[0][0]
