

#lista
lista_num = [100, 200, 300, 400, 500]


#Imprimir valores de uma lista
# for item in range(len(lista_num)):
#     lista_num[item] += 1000
#     print(lista_num[item])

def imprime_lista():
    for item, vlr in enumerate(lista_num):
        lista_num[item] += 1000
        print(lista_num[item])

