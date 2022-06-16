# lista_1 = [1, 2 ,3, 4]
# lista_2 = [3, 4, 5]

# intersection = set(lista_1) & set(lista_2)
# if len(intersection) >= 2:
#     print ("Parecidas")
# else:
#     print("No coinciden")

list_1 = [1, 2, 3, 4, 5]
list_2 = [2, 3, 4]

counter = 0

for x in range(len(list_1)):
    for i in range(len(list_2)):
        if list_1[x] == list_2[i]:
            counter +=1

if counter >= 2:
    print("Parecidas")
else:
    print("No coinciden")
    

# for x in list_1:
#     for i in list_2:
#         if x==i:
#             counter +=1



#OTRA FORMA
# print("Parecidas") if counter > 1 else print("No coinciden")