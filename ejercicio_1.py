lista_1 = [1, 2 ,3, 4]
lista_2 = [3, 4, 5]

intersection = set(lista_1) & set(lista_2)
if len(intersection) >= 2:
    print ("Parecidas")
else:
    print("No coinciden")