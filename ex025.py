#EXERCÍCIO 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
nome = str(input('Digite seu nome completo: ')).strip()
print(f'Você possui "Silva" em seu nome? True para SIM / False para NÃO ---> {'Silva' in nome.upper() }')