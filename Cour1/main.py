
import time
import random
from time import sleep
import pygame
from pygame import key, surface
from pygame.surface import Surface
from Cour1.assets import anim


pygame.init()

display = pygame.display.set_mode((800, 700))
ico = pygame.image.load("icone.png")
pygame.display.set_caption("Jeu de fou")
clock = pygame.time.Clock()
running = True

class Player():

    def __init__(self):
        self.image = pygame.image.load("player.png")
        self.player_box = pygame.transform.scale(self.image, (35, 60))
        self.rect = self.image.get_rect()
        self.positionx = 185
        self.positiony = 380


class Bouton:
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.SysFont('Arial', 30)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.text:
            texte_surface = self.font.render(self.text, True, (255, 255, 255))
            texte_rect = texte_surface.get_rect(center=self.rect.center)
            display.blit(texte_surface, texte_rect)


player = Player()
bouton_start = Bouton("black", 350, 200, 100, 50, "start")
bouton_credits = Bouton("black", 350, 400, 100, 50, "credit")
bouton_exit = Bouton("red", 350, 600, 100, 50, "exit")
random_color = "white"
random_x = random.randint(0, display.get_width() - ico.get_width())
random_y = random.randint(0, display.get_height() - ico.get_height())
menu = "on"

# animations :
anim = anim.Animation()
playerLeft = anim.anime_left()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if event.type == pygame.MOUSEMOTION: #position of the mouse
        #     print(event.pos)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu == "on":
                # Si on clique sur le bouton, on ferme le menu
                if bouton_start.rect.collidepoint(event.pos):
                    menu = "off"
                if bouton_credits.rect.collidepoint(event.pos):
                    menu = "credit"
                if bouton_exit.rect.collidepoint(event.pos):
                    running = False

    display.fill(random_color)
    keys = pygame.key.get_pressed()

    if menu == "on":
        bouton_start.draw(display)
        bouton_credits.draw(display)
        bouton_exit.draw(display)

    elif menu == "credit":
        display.blit(ico, (random_x, random_y))
        if keys[pygame.K_ESCAPE]:
            menu = "on"
        if keys[pygame.K_SPACE]:
            random_x = random.randint(0, display.get_width() - ico.get_width())
            random_y = random.randint(0, display.get_height() - ico.get_height())

    else:
        # Le jeu commence : on affiche le joueur à la souris
        display.blit(player.player_box, (player.positionx, player.positiony))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        display.fill(random_color)
        player.positionx = player.positionx - 5
        display.blit(playerLeft, (player.positionx, player.positiony))

    if keys[pygame.K_RIGHT]:
        player.positionx = player.positionx + 5
    if keys[pygame.K_UP]:
        player.positiony = player.positiony - 5
    if keys[pygame.K_DOWN]:
        player.positiony = player.positiony + 5
    if keys[pygame.K_SPACE]:
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        time.sleep(0.1)
    if keys[pygame.K_a]:
        random_color = "white"
    if keys[pygame.K_q]:
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        display.fill(random_color)
    if keys[pygame.K_ESCAPE]:
        menu = "on"

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
