#EXERCÍCIO 033: Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.

#Nesse caso decidi fazer somente usando a lógica somente com IF e ELSE.
A = int(input('Digite um número ---> '))
B = int(input('Digite outro número ---> '))
C = int(input('Digite outro número ---> '))

if A > B:
    if A > C:
        if B > C:
            print(f'{A} é o maior número e {C} é o menor número ')
        else:
            if B < C:
                print(f'{A} é o maior número e {B} é o menor número ')

if B > A:
    if  B > C:
        if A > C:
            print(f'{B} é o maior número e {C} é o menor número ')
        else:
            if C > A:
                print(f'{B} é o maior número e {A} é o menor número')

if C > A:
    if C > B:
        if A > B:
            print(f'{C} é o maior número e {B} é o menor número ')
        else:
            if B > A:
                print(f'{C} é o maior número e {A} é o menor número ')

