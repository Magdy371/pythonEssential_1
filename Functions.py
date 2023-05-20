def message(number):
    print("You have {} new messages".format(number))
# possisional parameters passing
def message_2(number, name):
    print("Hello {}, you have {} new messages".format(name, number))
# keyword argument passing
def introduction(name, age):
    print("Hello my name is {} and I am {} years old".format(name, age))

message(10)
message_2(10, "John")
introduction(age=10, name="John")