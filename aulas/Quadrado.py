

class Quadrado:


    def __init__(self):
        self._altura = 0
        self._comprimento = 0

    # def set_altura(self, a):
    #     if (not(isinstance(int, a) and (a > 0))):
    #        raise ValueError("Valor de altura inválido: {}".format(a))
    #     self._altura = a
    #
    # def set_comprimento(self, c):
    #     if (not(isinstance(int, c) and (c > 0))):
    #        raise ValueError("Valor de comprimento inválido: {}".format(c))
    #     self._comprimento = c

    def _set_altura(self, a):
        self._altura = a

    def _set_comprimento(self, b):
        self._comprimento = b

    def _get_area(self):
        return self._comprimento * self._altura

    def _get_perimetro(self):
        return 2 * self._comprimento + 2 * self._altura

    altura = property(fget=None, fset=_set_altura)
    comprimento = property(fget=None, fset=_set_comprimento)
    area = property(fget=_get_area)
    perimetro = property(fget=_get_perimetro)



quadr = Quadrado()
quadr.comprimento = 10
quadr.altura = 10

print(quadr.area)
print(quadr.perimetro)

quadr.altura = 20
quadr.comprimento = 20

print(quadr.area)
print(quadr.perimetro)


