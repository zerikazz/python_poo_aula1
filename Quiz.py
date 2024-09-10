from typing import List

class Quiz:
    __acertos : int
    __erros : int

    def __init__(self, acertos : int, erros : int):
        self.__acertos = acertos
        self.__erros = erros

    def get_acertos(self):
        return self.__acertos

    def get_erros(self):
        return self.__erros

    def calcular_pontos(self):
        return self.__acertos - self.__erros

    def __str__(self):
        info = f'Acertos {self.__acertos}'
        info += f'Total de pontos = {self.calcular_pontos()}\n'
        return info

class Quiz2A(Quiz):

    def __init__(self,acertos, erros):
        super().__init__(acertos, erros)

    def calcular_pontos(self):
        return self.get_acertos() - (4* self.get_erros())

class Quiz3A(Quiz):

    def __init__(self, acertos, erros):
        super().__init__(acertos, erros)

    def calcular_pontos(self):
        return self.get_acertos() - (2* self.get_erros())

class Aluno:
    __matricula : int
    __nome : str
    __quizes : List[Quiz]

    def __init__(self, m : int, n: str, kahoots : List[Quiz]):
        self.__matricula = m
        self.__nome = n
        self.__quizes = kahoots

    def __str__(self):
        info = f'Matricula: {self.__matricula}\n'
        info = f'Nome: {self.__nome}\n'
        total = 0
        for q in self.__quizes:
            total += q.calcular_pontos()
        info += f'Total de pontos = {total}\n'
        return info

