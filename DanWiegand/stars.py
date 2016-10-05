# Part 1

x = [1,5,13,3,25]
def drawStars(l):
   for val in l:
       if val == '':
           print val[0][0]
       else:
           print '*'*val
print drawStars(x)

# part 2

x = [1,4,"Bob",9,"Charlie",49,23]
def drawStars2(l):
   for val in l:
       if isinstance(val, int):
           print val*'*'
       else:
           print val[0] * len(val)

drawStars2(x)
