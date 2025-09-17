# EXERCÍCIO 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu
import random
maquina = random.randint(0,5)
print('BEM-VINDO!! ESSE É O JOGO DA ADIVINHAÇÃO, TENTE SER MELHOR QUE A MÁQUINA E DESCUBRA QUAL O NÚMERO ELA PENSOU ENTRE 0 E 5 \n VOCÊ CONSEGUIRÁ SUPERAR OS AVANÇOS DA TECNOLOGIA E SUPERAR ESSA INCRÍVEL MAQUINÁ SENCIENTE??? \n LHE DESEJO BOA SORTE MEU QUERIDO COMPANHEIRO HUMANO, USE AO MÁXIMO SEUS LINDOS NEURÔNIOS HAHAHAHAHAH')
jogador = input('Entre 0 e 5, o caos começou, \n qual o número que o bug invocou? ')
if jogador == maquina:
    print('MEUS PARABÉNS MEU QUERIDO MAMÍFERO EVOLUÍDO :) \n NÃO TEMOS PRÉMIO ENTÃO PODE IR EMBORA')
else:
    print('QUE TRISTEZA, A TECNOLOGIA VENCENDO A HUMANIDADE OUTRA VEZ :( \n SAIA DAQUI E DEIXE OUTRA MAMÍFERO COM COMPLEXO DE DEUS TENTAR \n ADEUS')
