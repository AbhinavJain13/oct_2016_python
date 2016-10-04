def insert(list):
    for i in range(1, len(list)):
        value = list[i]
        index = i - 1
        while i >= 0:
            if value < list[index]:
                list[index+1] = list[index]
                list[index] = value
                i = i - 1
            else:
                break
        print a
a = [1,5,2,4,8,6]
insert(a)
