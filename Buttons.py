# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 15:02:03 2023

@author: amaad
"""

import pygame

# Initialize pygame
pygame.init()

# Set screen size
screen = pygame.display.set_mode((1920, 1080))

# Create quit button
quit_button = pygame.Surface((100, 50))
quit_button.fill((255, 0, 0)) # Red color
quit_rect = quit_button.get_rect(center=(400, 300))
#x_button
#y_button
#z_button: "if button is pressed, store a variable(bool) that is true or false
#z_pressed=false
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for mouse click event on quit button
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if quit_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    screen.blit(quit_button, quit_rect)
    pygame.display.update()