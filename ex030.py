#EXERCÍCIO 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print('=' * 20)
print(' ' * 3, 'PAR OU ÍMPAR', ' ' * 4)
print('=' * 20)

par_impar = int(input('Digite um número inteiro e irei te dizer se é Ímpar ou Par ---> '))
if par_impar % 2 == 0:
    print('PAR')
else:
    print('ÍMPAR')
