foods = ["apples", "bread", "cheese", "milk", "bananas", "graves"]

# Bucle FOR:
for food in foods:
    if food == "cheese":
        print("you have to buy this")
        break # salimos del bucle
        # continue # volvemos al principio, no imprime food
    print(food)

for number in range(1, 8):
    print(number)

for letter in "hello":
    print(letter)

# Bucle WHILE:

count = 0
while count <= 10:
    print(count)
    count = count + 1