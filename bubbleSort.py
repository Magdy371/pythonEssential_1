# using bubble sort to sort a list of numbers
my_list = []
list2 = [32, 5, 3, 2, 1, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
NOE = int(input("Enter the number of elements: "))
for i in range(NOE):
    my_list.append(int(input("Enter the number: ")))
print(my_list)
swapped = True
counter = 0
while swapped:
    swapped = False
    for i in range(len(my_list)-1):
        if my_list[i] > my_list[i+1]:
            counter+=1
            swapped = True
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
print("The sorted list: ",my_list)
print("The number of swaps: ",counter)
#the big O notation for bubble sort is O(n^2)
# we can use sort method to sort the list
list2.sort()
print("The sorted list2: ",list2)