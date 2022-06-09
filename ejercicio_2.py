# dictionary = {}

# name = {"nombre": input("Nombre: ")}
# dictionary.update(name)
# print(list(dictionary.values()))

# age = {"edad": input("Edad: ")}
# dictionary.update(age)
# print(list(dictionary.values()))

# gender = {"sexo": input("Sexo: ")}
# dictionary.update(gender)
# print(list(dictionary.values()))

persona = {}

c = True

while c:
    clave = input("Dato a introducir: ")
    valor = input(clave + ": ")
    persona[clave]= valor
    print(persona)
    c = input("¿Quiere añadir un nuevo dato? 1-Si / 0-No ") == "1"