# Son inmutables
# Las tuplas son mucho más rápidas que las listas
x = (1, 2, 3)
print(x)
print(type(x))

y = tuple((1, 2, 3))
print(y)

# Tupla de un solo elemento:
z = (1,)
print(z)

w = (1, 2, 3, 4, 5)
print(w[1])

# w[4] = 10 # ERROR, la tupla es inmutable

# Eliminamos la tupla:
del w

# Usos de tuplas:

locations = {
    (35.1212, 54.6767): "Tokyo",
    (42.4234, 38.3456): "New York"
}