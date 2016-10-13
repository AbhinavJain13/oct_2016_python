# # Part I
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# for i in students:
#     name=""
#     for val in i.values():
#         if (name):
#             name+=" "+val
#         else:
#             name+=val
#     print (name)

# Part II
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
for key, data in users.items():
    print (key)
    for i in data:
        name=""
        count=1
        for val in i.values():
            if (name):
                name+=" "+val
            else:
                name+=val

        print (count,"-",name,"-",len(name)-1)
        count+=1
