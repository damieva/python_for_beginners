# Comparar números
x = 30
if x < 20:
    print("x is less than 20")
else:
    print("x is greater than 20")

# Comparar String
color = "blue"
if color == "red":
    print("color is red")
elif color == "blue":
    print("color is blue")
else:
    print("any color")

# Condiciones anidadas
name = "Jhon"
lastName = "Carter"
if name == "Jhon":
    if lastName == "Carter":
        print("You are Jhon Carter")
    else:
        print("You are not Jhon Carter")
else:
    print("You are not Jhon")


x = 3
y = 4
# Operadores:
if x > 2 and x <= 10:
    print("x is greater than two and less than or equal to ten")

if x > 2 or x <= 20:
    print("x is greater than two or less than or equal to twenty")

if (not(x == y)):
    print("x is not equal y")