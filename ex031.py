#EXERCÍCIO 031: Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagens de até 200KM e R$ 0,45 para viagens mais longas.
distancia = float(input('Qual a distância da viagem? Coloque em KM ---> '))
if distancia <= 200:
    preco = distancia * 0.50
    print(f'O preço da sua viagem será de R${preco:.2f}')
else:
    if distancia > 200:
        preco = distancia * 0.45
        print(f'O preço da sua viagem será de R${preco:.2f}')



