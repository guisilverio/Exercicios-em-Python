#EXERCÍCIO 021: Faça um programa em python que abra e reproduza o aúdio de um arquivo MP3.
import pygame
pygame.init()
pygame.music.load('endereço')
pygame.mixer.music.play()
pygame.event.wait()
