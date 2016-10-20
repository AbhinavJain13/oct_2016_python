import re, bcrypt

def gen_password(password):
    print('*'*20)
    print('PASSWORD ENCRYPTION IN PROCESS...')
    print('*'*20)
    print(bcrypt.hashpw(password,bcrypt.gensalt()))
    return bcrypt.hashpw(password.encode(),bcrypt.gensalt())

def validate_email(email):
    print('*'*20)
    print('VALIDATING EMAIL...')
    print('*'*20)

    if re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', email):
        print('*'*20)
        print('EMAIL MATCH!!')
        print('*'*20)
        return(True)
    else:
        print('*'*20)
        print('EMAIL FAIL!!')
        print('*'*20)
        return(False)

def validate_length(strng,length):
    print('*'*20)
    print('VALIDATING STRING LENGTH...')
    print('*'*20)
    if len(strng) >= length:
        print('*'*20)
        print('LENGTH VALID!!')
        print('*'*20)
        return(True)
    else:
        print('*'*20)
        print('LENGTH NOT VALID!!')
        print('*'*20)
        return(False)

def validate_letters(strng,length):
    print('*'*20)
    print('VALIDATING STRING...')
    print('*'*20)
    if len(strng) > length and isinstance(strng, basestring):
        print('*'*20)
        print('CHARS VALID!!')
        print('*'*20)
        return(True)
    else:
        print('*'*20)
        print('CHARS NOT VALID!!')
        print('*'*20)
        return(False)

def match_strings(s1,s2):
    print('*'*20)
    print('MATCHING STRINGS...',s1,s2)
    print('*'*20)
    if str(s1) == str(s2):
        print('STRINGS MATCH!')
        return True
    else:
        print('STRINGS DONT MATCH!')
        return False
