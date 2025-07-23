#EXERCÍCIO 024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
cidade = str(input('Informe o nome da sua cidade: ')).strip()

print(f'O nome da sua cidade começa com "Santo"? True para SIM / False para NÃO ---> {cidade[:5].upper() == 'SANTO'}')