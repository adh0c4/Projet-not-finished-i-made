#First of all, type "python3 -m pip install -U pygame==2.6.0" on the CMD or any other terminal

import pygame
import assets.Mouvements
pygame.init()



#Screen of the game
img = pygame.image.load('icone.ico')
clock = pygame.time.Clock()
pygame.display.set_icon(img)
pygame.display.set_caption("baptiste adventure")
screen = pygame.display.set_mode((400, 500))
running = True


#player
class Player(assets.Mouvements.anim) : 
    
    def __init__(self):
        
        self.image = pygame.image.load('assets/Sprites/player/player.png')
        self.baptiste = pygame.transform.scale(self.image, (35, 60))
        self.rect = self.image.get_rect()
        self.positionx = 185
        self.positiony = 380

    def anim_back(self):
        super().__init__("playerfront")
        self.start_animation()
        self.animate()
        
#loading player
player = Player()

#keep the screen open
while running:
    screen.fill("white")

    #show the player
    screen.blit(player.baptiste, (player.positionx, player.positiony))


    # For close the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.positionx > 0:
        player.positionx -= 5
        
    if keys[pygame.K_RIGHT] and player.positionx < 370:
        player.positionx += 5
    if keys[pygame.K_UP]:
        player.positiony -= 5
        player.anim_back()
    if keys[pygame.K_DOWN] and player.positiony < 440:
        player.positiony += 5

    
    
    #usefull stuffs
    # print(positionx, positiony) #position of the player
    # if event.type == pygame.MOUSEMOTION: #position of the mouse
    #     print(event.pos)

    pygame.display.update() 
    pygame.display.flip()
    
    clock.tick(60)  # limits FPS to 60
pygame.quit()




