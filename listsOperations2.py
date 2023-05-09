# inner life of the list
list1 = [1, 2, 3, 4, 5]
print("list1: ",list1)
print("id(list1): ",id(list1))
list2 = list1
print("list2: ",list2)
print("id(list2): ",id(list2))
list1[0] = 10
print("list1: ",list1)
print("list2: ",list2)
###
#slice operator
my_list = [1, 2, 3, 4, 5]
print("my_list: ",my_list)
print("my_list[1:3]: ",my_list[1:3])
print("my_list[:3]: ",my_list[:3])
print("my_list[:]: ",my_list[:])
# negative slice index
print("my_list[-3:-1]: ",my_list[-3:-1])
print("my_list[-3:]: ",my_list[-3:])
###
# more about del instruction
# del instruction can be used to delete a slice from a list or clear the entire list
# del instruction can also be used to delete entire variables
# 
my_list = [1, 2, 3, 4, 5]
print("my_list: ",my_list)
del my_list[1:3] 
print("my_list after del instruction : ",my_list)
# del my_list will delete the list itself not the content of the list only.
del my_list
#print("my_list after del instruction : ",my_list) will cause run time error
###
# in and not in operators
# in and not in operators can be used to check if a value is in a list or not
my_list = [1, 2, 3, 4, 5]
print("my_list: ",my_list)
print("3 in my_list: ",3 in my_list)
print("3 not in my_list: ",3 not in my_list)