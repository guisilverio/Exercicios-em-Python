#EXERCÍCIO 008: CONVERSOR DE MEDIDAS --> Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.
print('=' * 40)
print ('C O N V E R S O R  D E  M E D I D A S '.center(40))
print('=' * 40)
M = float(input('Coloque a medida em Metros: '))
C = M * 100
Mili = M * 1000
print(f'Centímetros = {C:.2f} cm')
print(f'Milímetros = {Mili:.2f} mn')