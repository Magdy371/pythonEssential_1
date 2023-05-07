var = 17
var_right = var >> 1
var_left = var << 2
print("var_right: ",var_right)
print("var_left: ",var_left) 
print("var: ",var)
x = 4
y = 1
 
a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2
 
print(a, b, c, d, e, f)