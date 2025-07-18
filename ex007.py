#EXERCÍCIO 007: MÉDIA ARITMÉTICA --> Desenvolva um programa que leia as duas notas de um aluno e calcule a média aritmética.
print('=' * 40)
print('M É D I A  A R I T M É T I C A'.center(40))
print ('=' * 40)

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A média foi de: {m:.1f}')
