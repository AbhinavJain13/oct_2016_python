# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
#
# for value in students:
#     print value['first_name'], value['last_name']


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
def getPeople(users):
    print 'Students'
    count = 0
    for student in users['Students']:
        name = student['first_name'].upper() + " " + student['last_name'].upper()
        length = len(student['first_name']) + len(student['last_name'])
        count +=1
        print "{} - {} - {}".format(count, name, length)
    print 'Instructors'
    incount = 0
    for instructor in users['Instructors']:
        inname = instructor['first_name'].upper() + " " + instructor['last_name'].upper()
        inlength = len(instructor['first_name']) + len(instructor['last_name'])
        incount += 1
        print "{} - {} - {}".format(incount, inname, inlength)
getPeople(users)
