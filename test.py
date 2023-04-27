#knowing the end time period knowing the number of minutes
hourse = int(input("Enter the begining of hour: "))
minutes = int(input("Enter the begining of minutes: "))
minutes_ned = int(input("Enter the number of dura needed: "))
minutes_total = minutes + minutes_ned
hourse_total = hourse + minutes_total // 60
minutes_total = minutes_total % 60
print("The time after", minutes_ned, "minutes is", hourse_total, ":", minutes_total)