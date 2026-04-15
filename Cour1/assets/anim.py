
import time
import pygame

def load_sprite(path, size=None):
    image = pygame.image.load(path).convert_alpha()
    if size:
        image = pygame.transform.scale(image, size)
    return image

class Animation(pygame.sprite.Sprite) :
    def __init__(self):
        self.playerback1 = pygame.image.load("assets/Sprites/player/playerback1.png").convert_alpha()
        self.playerback2 = pygame.image.load("assets/Sprites/player/playerback2.png").convert_alpha()
        self.playerfront1 = load_sprite("assets/Sprites/player/playerfront1.png", (35, 60))
        self.playerfront2 = load_sprite("assets/Sprites/player/playerback2.png", (35, 60))
        self.playerleft1 = pygame.image.load("assets/Sprites/player/playerleft1.png").convert_alpha()
        self.playerleft2 = pygame.image.load("assets/Sprites/player/playerleft2.png").convert_alpha()
        self.playerright1 = pygame.image.load("assets/Sprites/player/playerright1.png").convert_alpha()
        self.playerright2 = pygame.image.load("assets/Sprites/player/playerright2.png").convert_alpha()

        # lists of sprites
        self.front = [pygame.transform.scale(self.playerleft1, (35, 60)),
                      pygame.transform.scale(self.playerleft2, (35, 60))]
        self.back = [self.playerback1, self.playerback2]
        self.left = [self.playerleft1, self.playerleft2]
        self.right = [self.playerright1, self.playerright2]
        self.animationIndex = 0
        self.rect = pygame.Rect(0, 0, 35, 60)

    def anime_front(self):
        self.animationIndex += 1

        if self.animationIndex >= len(self.front):
            self.animationIndex = 0

        surf = self.front[self.animationIndex]
        return surf

    def anime_back(self):
        self.animationIndex += 1

        if self.animationIndex >= len(self.back):
            self.animationIndex = 0

        self.surf = self.back[self.animationIndex]

    def anime_left(self):
        time.sleep(0.5)
        self.animationIndex += 1

        if self.animationIndex > len(self.left):
            self.animationIndex = 0

        surf = self.left[self.animationIndex]
        return surf

    def anime_right(self):
        self.animationIndex += 1

        if self.animationIndex >= len(self.right):
            self.animationIndex = 0

        self.surf = self.right[self.animationIndex]
