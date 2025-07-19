#EXERCÍCIO 020: O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostra a ordem sorteada.
import random
N1 = input('Informe seu nome ---> ')
N2 = input('Informe seu nome ---> ')
N3 = input('Informe seu nome ---> ')
N4 = input('Informe seu nome ---> ')

print(f'Está será à ordem de apresentação: \n {random.sample([N1,N2,N3,N4], k=4 )}')