#EXERCÍCIO 016: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua posição inteira.
from math import trunc
numero = float(input('Digite um número quebrado. \n EX: 3.5; 4.8; 0,25 \n =' ))

print(f'O número {numero} tem a parte inteira {trunc(numero)}')

