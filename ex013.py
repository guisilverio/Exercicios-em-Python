#EXERCÍCIO 013: REAJUSTE SALARIAL --> Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário com 15% de aumento.
Sal_Atual = float(input('Informe o valor do seu salário atual: '))
Aumento = Sal_Atual * (15/100)
print(f'Você terá 15% de aumento, o que consiste em {Aumento:.2f} R$ de aumento no seu salário. ')
Sal_CAumento = Sal_Atual + Aumento
print (f'Seu novo salário será de {Sal_CAumento:.2f} R$.')