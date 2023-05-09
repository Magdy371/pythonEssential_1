my_list = [17 , 3 , 11 , 5 , 1 , 9 , 7 , 15 , 13]
largest = my_list[0]
for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]
print(largest)
### ANOTHER WAY TO DO IT ###
print("The largest number in the list is: ", max(my_list))
# found an element index in a list
element_to_found = int(input("Enter the element to be found: "))
e_found = False
for i in range(len(my_list)):
    e_found = my_list[i] == element_to_found
    if e_found:
        break
if e_found:
    print("Element found at index: ", i)
else:
    print("Element not found")
