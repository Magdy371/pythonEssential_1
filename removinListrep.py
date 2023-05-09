my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
repeated = False
length = len(my_list)-1
#removing repeated elements
for i in range(length):
    for j in range(i+1, length):
        if my_list[i] == my_list[j]:
            repeated = True
            my_list.pop(j)
            length -= 1
    if repeated:
        my_list.pop(i)
        length -= 1
    repeated = False
print(my_list)