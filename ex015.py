'''
EXERCÍCIO 015: ALUGUEL DE CARROS --> Faça um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por KM rodado.
'''
KM = float(input('Quantos KMs foram percorridos? '))
D = int(input('Por quanto dias ele foi alugado? '))
Valor_KM = KM * 0.15
Valor_D = D * 60
VT = Valor_KM + Valor_D
print(f'O valor a ser pago por KM rodado é {Valor_KM} R$')
print(f'O valor a ser pago pelos dias alugado é {Valor_D} R$')
print(f'O valor total a ser pago será de {VT:.2f} R$')
