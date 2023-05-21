# return without an expression
def function1(whishes = True):
    print("I wish it is true")
    if not whishes:
        return
    print("I wish it is false")

function1()
function1(whishes=False)

# returb with an expression
def Integral(x):
    return x**2 + 2*x + 1

print(Integral(2))

#None is a special value in Python that represents the absence of a value or a null value.
#It is an object of its own datatype, the NoneType.
#We cannot create multiple None objects but can assign it to variables.
def string_function(s):
    if s%2 == 0:
        return "Even"
print(string_function(1))


# effects and result : functions and lists
def list_sum(lst):
    s = 0
    for elem in lst:
        s += elem
    return s
print(list_sum([1, 2, 3]))
# print(list_sum(5)) this will give an error