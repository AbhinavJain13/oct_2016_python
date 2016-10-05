# def bubbleSort(a):
#     for num in range(len(a)-1,0, -1):
#         for i in range(num):
#             if a[i]>a[i+1]:
#                 a[i], a[i+1] = a[i+1], a[i]
# a = [54,26,93,17,77,31,44,55,20]
# bubbleSort(a)
# print(a)

# why does thee code above work, starting from the end of the list and moving to the start, but below doesnt? moving from the start of the list to the end.
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
def bubbleSort(my_list):
    for num in range(len(my_list)):
        for i in range(num):
            if my_list[i]>my_list[i+1]:
                temp = my_list[i]
                my_list[i] = my_list[i+1]
                my_list[i+1] = temp
my_list = [54,26,93,17,77,31,44,55,20]
bubbleSort(my_list)
print(my_list)
