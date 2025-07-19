#EXERCÍCIO 018: Faça um programa que leia um ângulo qualquer e mostra na tela o valo do seno, cosseno e tangente desse ângulo.
import math
A = int(input('Informe o ângulo ---> '))
Seno = math.sin(math.radians(A))
Cosseno = math.cos(math.radians(A))
Tangente = math.tan(math.radians(A))
print(f'O cosseno é: {Cosseno:.4f} \n O seno é: {Seno:.4f} \n O tangente é: {Tangente:.4f}')