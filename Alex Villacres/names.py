students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for value in students:
    print value['first_name'], value['last_name']

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



def getPeople(l):
    student_count = 0
    teacher_count = 0
    print "Students"
    for student in users['Students']:
        student_count += 1
        name_chars = len(student['first_name']) + len(student['last_name'])
        print "{} - {} {} - {}".format(student_count, student['first_name'].upper(), student['last_name'].upper(), name_chars)
    print "Instructors"
    for instructor in users['Instructors']:
        teacher_count += 1
        name_chars = len(instructor['first_name']) + len(instructor['last_name'])
        print "{} - {} {} - {}".format(teacher_count, instructor['first_name'].upper(), instructor['last_name'].upper(), name_chars)

getPeople(users)
