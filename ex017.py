#EXERCÍCICO 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente, calcule e mostre o comprimento da hipotenusa.
import math

CA = float(input('Digite o comprimento do cateto adjacente ---> '))
CO = float(input('Digite o comprimento do cateto oposto ---> '))
H = (CA * CA) + (CO * CO)
H = H ** (1/2)
print(f'O comprimento da hipotenusa é: {H:.2f} cm')



#Resolvendo o exercício utilizando módulos.
Cateto_Adjacente = float(input('Digite o comprimento do cateto adjacente ---> '))
Cateto_Oposto = float(input('Digite o comprimento do cateto oposto ---> '))
Hipotenusa = math.pow(Cateto_Adjacente,2) + math.pow(Cateto_Oposto,2)
Hipotenusa = math.sqrt(Hipotenusa)
print(f'O comprimento da hipotenusa é {Hipotenusa:.2f} cm')



''