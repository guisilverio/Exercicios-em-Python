#EXERCÍCIO 014: CONVERSOR DE TEMPERATURAS --> Escreva um programa que converta uma temperatura digitada em °C e converta para °F.
C = float(input('Informe a temperatura em °C: '))
F = (C * 1.8) + 32
print(f'A temperatura em Fahrenheit é de {F:.1f} °F')
