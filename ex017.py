#EXERCÍCICO 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente, calcule e mostre o comprimento da hipotenusa.
import math


CA = float(input('Digite o comprimento do cateto adjacente ---> '))
CO = float(input('Digite o comprimento do cateto oposto ---> '))
H1 = (CA * CA) + (CO * CO)
H2 = H1 ** (1/2)
print(f'O comprimento da hipotenusa é: {H2:.2f} cm')



#Resolvendo o exercício utilizando módulos.
Cateto_Adjacente = float(input('Digite o comprimento do cateto adjacente ---> '))
Cateto_Oposto = float(input('Digite o comprimento do cateto oposto ---> '))
Hipotenusa = math.pow(Cateto_Adjacente,2) + math.pow(Cateto_Oposto,2)
Hipotenusa = math.sqrt(Hipotenusa)
print(f'O comprimento da hipotenusa é {Hipotenusa:.2f} cm')


ca = float(input('Digite o comprimento do cateto adjacente ---> '))
co = float(input('Digite o comprimento do cateto oposto ---> '))
h = math.hypot(ca,co)
print(f'O comprimento da hipotenusa é {h:.2f} cm')
