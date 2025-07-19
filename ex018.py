#EXERCÍCIO 018: Faça um programa que leia um ângulo qualquer e mostra na tela o valo do seno, cosseno e tangente desse ângulo.
import math
A = int(input('Informe o ângulo ---> '))
Seno_Radiantes = math.radians(A)
Cosseno_Radiantes = math.radians(A)
Tangente_Radiantes = math.radians(A)

Seno_graus = math.sin(Seno_Radiantes)
Cosseno_graus = math.cos(Cosseno_Radiantes)
Tangente_graus = math.tan(Tangente_Radiantes)

print(f'O cosseno é: {Cosseno_graus:.4f} \n O seno é: {Seno_graus:.4f} \n O tangente é: {Tangente_graus:.4f}')