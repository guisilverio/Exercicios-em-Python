#EXERCÍCIO 010: CONVERSOR DE MOEDAS --> Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quanto dólares ela pode comprar. Considere o dólar a 3,27.
R = float(input('Informe o quanto você tem em R$: '))
D = 3.27
C = R / D
print(f'Você consegue comprar {C:.2f} U$')
