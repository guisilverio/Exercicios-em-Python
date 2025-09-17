#EXERCÍCO 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada KM acima do limite.
velocidade = float(input('A qual velocidade estava o carro? Escreva em KM ---> '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você está acima da velocidade permitida! Irá receber um multa de R${multa:.2f}.')
else:
    if velocidade <= 80:
        print('Você está na velocidade permitida!!')
