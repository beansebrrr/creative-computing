"""
Learn pygame
"""

import pygame, sys

pygame.init()
clock = pygame.time.Clock()

# Window
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Balling")

while True:
    pygame.display.flip()