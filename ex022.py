'''
EXERCÍCIO 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
* O nome com todas as letras maiúsculas.
* O nome com todas as letras minúsculas.
* Quantas letras tem ao todo (sem considerar espaços).
* Quantas letras tem o primeiro nome.
'''

print('=' * 40)
print('A N A L I S A D O R  D E  T E X T O'.center(40))
print('=' * 40)
nome = str(input('Digite seu nome completo: ')).strip()
lista_nome = nome.split()
print(f'Seu nome com todas as letras maiúsculas ---> {nome.upper()}')
print (f'Seu nome com todas as letras minúsculas ---> {nome.lower()}')
print (f'Seu nome completo tem ---> {len(''.join(lista_nome))} letras (sem espaços)')
print(f'O seu primeiro nome tem ---> {len(lista_nome[0])} letras')

#Uma outra forma de resolver esse exercício após verificar a resolução no curso.
N = str(input('Digite seu nome completo: ')).strip() #Colocando o ".strip" aqui serve para eliminar qualquer espaço adicionado pelo usuário, no início ou final, antes de digitar realmente o nome completo.
print(f'Seu nome em maiúsculas é {N.upper()} ')
print(f'Seu nome em minúsculas é {N.lower()}')
print(f'Seu nome tem ao todo {len(N) - N.count(' ')}')
print(f'O seu primeiro nome tem {N.find(' ')}')
