import os
import warnings

# Suppress pygame warnings
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
warnings.filterwarnings('ignore')

import pygame

ANCHO = 1000
ALTO = 700

#Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

puntuacion=0
font = None

nivel_desbloqueado = 5
MAX_NIVELES = 5