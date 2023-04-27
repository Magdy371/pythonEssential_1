#knowing the maximum number of conditions
num = int(input("Enter the number of conditions: "))
#creating a list to store the conditions
conditions = []
#creating a list to store the results
results = []
#creating a list to store the final results
final = []
if num == 1:
    #if there is only one condition, the result is the condition itself
    conditions.append(input("Enter the condition: "))
    results.append(input("Enter the result: "))
    final.append(conditions[0])
    final.append(results[0])
else:
    #if there are more than one condition, the results are the conditions
    #themselves
    for i in range(num):
        conditions.append(input("Enter the condition: "))
        results.append(input("Enter the result: "))
        final.append(conditions[i])
        final.append(results[i])
#displaying the final results
print(final)
