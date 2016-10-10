# print 'hello world'

'''
name = raw_input()
def say_hello(name):

    if name:
        print 'hello ' + name
    else:
        print 'nooo name'
print 'outside the function'


age=raw_input()
if age >= 18:
  print 'Legal age'
elif age == 17:
  print 'One more year and you will be of legal age'
else:
  print 'You are so young!'


count=0
while count <5:
    print 'loopin -', count
    count +=1
'''

for val in [1,2,3,4,5]:
    if val == 3:
        # print 'break on: ',val
        continue
    print val
