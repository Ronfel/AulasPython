class MetEstatico:
    @staticmethod
    def func1():
        print("func1()")
    @staticmethod
    def func2(x, y):
        print("Função '{}' invocada. \nParams=({}, {})".format("func2", x, y))
    @staticmethod
    def func3(a, b, c):
        info = """
        Nome da Função {nome}
        Quantidade de Args {quantidade}
        Args: {args}
        """
        info = info.format(nome=MetEstatico.func3.__name__,
                    quantidade=MetEstatico.func3.__code__.co_argcount,
                    args=MetEstatico.func3.__code__.co_varnames
        )
        print(info)

    # func1 = staticmethod(func1)
    # func2 = staticmethod(func2)
    # func3 = staticmethod(func3)
    
me = MetEstatico
me.func1()
me.func2(700, 800)
me.func3(300, 400, 500)


