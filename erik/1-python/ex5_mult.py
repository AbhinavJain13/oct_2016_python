# read list, multiply each value by 5
data = [2,3,5,7,9]
def multlist(ary,mult):
    for idx, val in enumerate(ary):
        #print idx, val
        ary[idx] = ary[idx]*mult
    print ary

multlist(data,5)
