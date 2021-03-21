# Ejemplos: print, dir, type

def hello(name="Person"):
    print(f"Hello {name}")

hello("Denis")
hello("Kino")
# Parametro por defecto
hello()


def add(numberOne, numberTwo):
    return numberOne + numberTwo

print(add(10, 20))


# Lambda functions:

addLambda = lambda numberOne, numberTwo: numberOne + numberTwo
print(addLambda(10,20))