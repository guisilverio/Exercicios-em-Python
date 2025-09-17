#EXERCÍCIO 034: Escreva um programa que pergunta o sálario de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para salários inferiores ou iguais, o aumento é de 15%
salario = float(input('Qual o seu salário? ---> '))
if salario > 1250:
    aumento10 = salario * (10/100)
    salario_novo10 = aumento10 + salario
    print(f'O seu aumento será de R${aumento10:.2f} e seu novo salário será de R${salario_novo10:.2f}')
else:
    if salario <= 1250:
        aumento15 = salario * (15/100)
        salario_novo15 = salario + aumento15
        print(f'O seu aumento será de R${aumento15:.2f} e seu novo salário será de R${salario_novo15:.2f}')