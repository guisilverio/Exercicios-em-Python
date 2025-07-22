#EXERCÍCIO 024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
cidade = str(input('Informe o nome da sua cidade: '))
print(f'O nome da sua cidade possui "Santo" em sua composição? True para SIM / False para NÃO ---> {'Santo' in cidade}')