def names():
    users={
        'students': [
            {'first_name': "Michael", 'last_name': 'Jordan'},
            {'first_name': "John", 'last_name': 'Rosales'},
            {'first_name': 'Mark', 'last_name': 'Guillen'},
            {'first_name': 'KB', 'last_name': 'Tonel'}
        ],
        'Instructors': [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'Martin', 'last_name': 'Puryears'}
        ]
    }
    for x,y in users.items():
        count = 1
        print x
        for z in y:
            print count, z['first_name'], z['last_name'], '-', len(z['first_name'])+len(z['last_name'])
            count = count + 1
names()
