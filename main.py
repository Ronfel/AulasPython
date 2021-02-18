
import aula1
import aula2
import listas
import importlib
import recarregamodulo
from pprint import pprint
from sys import path as lpath

def teste_input():
    aula1.chama()

def teste_path():
    aula2.pprint(lpath)

def teste_lista():
    listas.imprime_lista()

recarregamodulo.a = 50
del(recarregamodulo.b)

importlib.reload(recarregamodulo)

pprint(recarregamodulo.a)

pprint(globals())


#teste_lista()
#teste()
