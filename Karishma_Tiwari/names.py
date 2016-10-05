# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
#
#
# #
# # for i in range(0, len(students)):
# #     for val in students[i].itervalues():
# #         print val
# for i in range(0, len(students)):
#     print students[i]['first_name'], students[i]["last_name"]
#

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

# for key, data in users.items():
#     for i in range(0, len('key')):
#         print i, users[key][i]["first_name"], users[key][i]["last_name"], - (len(users[key][i]["first_name"])+ len(users[key][i]["last_name"]))

for key, data in users.items():
    count = 0;
    for value in data:
        count +=1;
        full_name=value["first_name"]+ " "+ value["last_name"]
        full_name_upper = full_name.upper()
        counter = len(value["first_name"])+len(value["last_name"])

        print count, full_name_upper,counter
