numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list content:", numbers)  # Printing previous list content.

print("\nList's length:", len(numbers))  # Printing previous list length.

###

del numbers[1]  # Removing the second element from the list

# adding elements to the end of the list using the append() method
numbers.append(100)
numbers.append(500)
print("New list's content:", numbers)  # Printing current list content.
print("New list's length:", len(numbers))  # Printing new list length.

###
# adding elements to any of the list using the insert() method
numbers.insert(1, 200)
print("New list's content:", numbers)  # Printing current list content.
print("New list's length:", len(numbers))  # Printing new list length.
total = 0
#useing for loop to sum the elements in the list
for i in range(len(numbers)):
    total += numbers[i]
print("Total of the elements in the list:", total)
#useing sum() function to sum the elements in the list
sum = sum(numbers)
print("Total of the elements in the list:", sum)

# swap the elements in the list
for i in range(len(numbers)//2):
    numbers[i], numbers[len(numbers)-1-i] = numbers[len(numbers)-1-i], numbers[i]
print("New list's content:", numbers)  # Printing current list content.

### another method to swap the elements in the list
list2 = []
for i in range(len(numbers)):
    list2.append(numbers[len(numbers)-1-i])
print("New list's2 content:", list2)  # Printing current list content.

# useing the reverse() method to swap the elements in the list
#numbers.reverse()

