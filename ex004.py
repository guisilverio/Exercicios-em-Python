#EXERCÍCIO 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
txt = input('Digite algo: ')
print(f'O tipo primitivo do que você digitou é: {type(txt)}')
print(f'É um número? {txt.isnumeric()}')
print(f'É uma letra? {txt.isalpha()}')
print(f'É alfanúmerico? {txt.isalnum()}')
print(f'Está em maiúsculas? {txt.isupper()}')
print(f'É algum número decimal? {txt.isdecimal()}')
