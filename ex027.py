#EXERCÍCIO 027: Faça um programa que leia o nome de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite se nome completo: ')).strip()
dividido = nome.split()
print(f'O seu primeiro nome é: {dividido[0]}')
print(f'O seu último nome é: {dividido[-1]}')