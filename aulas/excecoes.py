#Exceções

def testedivisao(n1, n2):
    try:
        c = n1 / n2
        print(c)
    except ZeroDivisionError:
        print("Não divida um número por zero!")

def entrada():
    continua = True
    while continua:
       try:
           n1 = int(input("Insira um número: "))
           n2 = int(input("Insira outro número: "))
       except ValueError:
           print("Fim da aplicação")
           continua = False
       else:
           testedivisao(n1, n2)
       finally:
           print()
           print("-----------------------")
           print()

entrada()


