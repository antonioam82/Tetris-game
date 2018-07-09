import random
import time
import pygame
import sys
from pygame.locals import *
from constantes import *

class Juego(object):
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(TAMAÑO_VENTANA)
        self.fuentes = {
            'predeterminada': pygame.font.Font('fressansbold.ttf', 18),
            'titulo': pygame.font.Font('fressansbold.ttf', 100),
        }
        pygame.display.set_caption('Aplicación Tetris')
