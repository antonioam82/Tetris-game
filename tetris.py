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

def start(self):
    self._mostrarTexto('Tetris', CENTRO_VENTANA, fuente='titulo')
    self.mostrar_Texto('Pulse una tecla...', POS)
    self.espera()

def stop(self):
    sel.mostrarTexto('Ha perdido', CENTRO_VENTANA, fuente='titulo')
    self.espera()
    self.salir()

def _mostrarTexto(self, texto, posicion, color=9, fuente='predeterminada'):
    print("Mostrar  texto")
    fuente = self.fuentes.get(fuente, self.fuentes['predeterminada'])
    color = COLORES.get(color, COLORES[9])
    repres = fuente.render(texto, True, color)
    rect = repres.get_rect()
    rect.center = posicion
    self.surface.blit(repres, rect)

def _espera(self):
    print("Espera")
    while self._getEvent() == None:
        self._restituir()

def restituir(self):
    pygame.display.update()
    self.clock.tick()

def _getEvent(self):
    for event in pygame.event.get():
        if event.type==QUIT:
            self.salir()
        if event.type==KEYUP:
            if event.key==K_ESCAPE:
                self._salir()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                continue
            return event.key

def salir(self):
    print("Salir")
    pygame.quit()
    sys.exit()
    
def getPiece(self):
    return PIEZAS.get(random.choice(PIEZAS_KEYS))
def _getCurrentPieceColor(self):
    for l in self.current[0]:
        for c in l:
            if c!=0:
                return c

def _calcularDatosPiezasEnCurso(self):
    m=self.current[self.position[2]]
    coords=[]
    for i in enumerate(m):
        for j, k in enumerate(l):
            if k!=0:
                coords.append([i+self.position[0],j+self.position[1]])
        self.coordenadas=coords
