#EXERCÍCICO 006: Crie um programa que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = float(input('Digite um número: '))
d = n * 2
t = n * 3
rq = n ** (1/2)
print(f'O dobro de {n} é: {d:.0f}')
print(f'O triplo de {n} é: {t:.0f}')
print(f'A raiz quadrada de {n} é: {rq:.2f}')

