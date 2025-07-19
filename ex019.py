#EXERCÍCIO 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random

N1 = input('Informe seu nome ---> ')
N2 = input('Informe seu nome ---> ')
N3 = input('Informe seu nome ---> ')
N4 = input('Informe seu nome ---> ')

print(random.choice([N1, N2, N3, N4]))