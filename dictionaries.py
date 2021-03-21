# Clave: Valor

# Creación:
product = {
    "name": "book",
    "quantity": 3,
    "price" : 4.99
}

print(type(product))
#print(dir(product))

# Obtener las claves:
print(product.keys())

# Obtener items:
print(product.items()) # Los valores van dentro de una tupla y el conjunto dentro de una lista

# Limpiar:
product.clear()
print(product)

# Eliminar:
del product

# Uso común:
products = [
    {"name": "book", "price": 10.99},
    {"name": "laptop", "price": 1000}
]
print(type(products))
print(products)