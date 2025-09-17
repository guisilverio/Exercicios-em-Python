#EXERCÍCIO 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
l1 = int(input('Digite qual o comprimento da reta N° 1 ---> '))
l2 = int(input('Digite qual o comprimento da reta N° 2 ---> '))
l3 = int(input('Digite qual o comprimento da reta N° 3 ---> '))
if l1 + l2 > l3:
    if l2 + l3 > l1:
        if l3 + l1 > l2:
            print('As retas formam um triângulo :) ')
else:
    print('As retas não formam um triângulo :( ')
