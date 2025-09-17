#EXERCÍCIO 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = str(input('Informe o ano ---> '))
if ano[2:4] == '00':
    if int(ano) % 400 == 0:
        print('O ano é BISSEXTO')
    else:
        print('O ano NÃO É BISSEXTO')

if ano[2:4] != '00':
    if int(ano) % 4 == 0:
        print('O ano é BISSEXTO')
    else:
        print('O ano NÃO É BISSEXTO')














