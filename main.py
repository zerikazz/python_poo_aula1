
from Quiz import *

if __name__ == "__main__":
    q1 = Quiz(10, 2) #resultado esperado 8
    print(q1)
    q2 = Quiz2A(10, 2) #resultado esperado 2
    print(q2)
    q3 = Quiz3A(10, 2) #resultado esperado 6
    print(q3)

    lista_quiz = [q1, q2, q3]

    aluno1 = Aluno(1, "Marquinhos", lista_quiz)
    print(aluno1)
