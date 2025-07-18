#CALCULANDO DESCONTO: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
PP = float(input('Informe o preço do produto: '))
D = PP * (5/100)
print(f'O valor do desconto é de {D:.2f} R$.')
Preco_CDesconto = PP - D
print(f'O preço do produto com desconto é de {Preco_CDesconto:.2f} R$.')
