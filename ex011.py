'''
EXERCÍCIO 011: PINTANDO PAREDE --> Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-lo, sabendo que cada litro de tinta, pinta uma área de 2m².
'''

larg = float(input('Informe a largura da parede em metros: '))
alt = float(input('Informe a altura da parede em metros: '))
area = larg * alt
print(f'A área da parede é de {area} m²')
tinta = area / 2
print(f'A quantidade de tinta necessário para pintar a parede será de: {tinta:.2f} litros.')
