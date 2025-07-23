'''

EXERCÍCIO 026: Faça um programa que leia uma frase pelo teclado e mostre:
* Quantas vezes aparece a letra "a".
* Em que posição ela aparece a primeira vez.
*Em que posição ela aparece a última vez.
'''
frase = str(input('Digite um texto qualquer: ')).strip()
print(f'A letra "a" apareceu {frase.upper().count('A')} vezes.')
print(f'Ela apareceu a primeira vez na frase no índice {frase.upper().find('A')+1}')
print(f'Ela apareceu pela última vez na frase no índice {frase.upper().rfind('A')+1}')
