
import pygame

class anim(pygame.sprite.Sprite) :

    def __init__(self, sprite_name):
        super().__init__()
        # self.image = pygame.image.load('assets/Sprites/' + sprite_name + '/' + sprite_name + '.png')
        self.first_sprite = 0
        self.images = animations.get(sprite_name)
        
        self.animation = False
    


    def start_animation(self):
        self.animation = True


    def animate(self) : 
        if self.animation :

            self.first_sprite += 1

            if self.first_sprite > len(self.images):
                self.first_sprite = 0
                self.animation = False

            self.image = self.image[self.first_sprite]

#dont load out of the class will creat many of bugs and shits like that 
def load_anim(sprite_name) :
    image_list = []
    path = f"assets/Sprites/{sprite_name}/{sprite_name}"

    #will load the images in the list by the path of each sprites
    #The way i stocked the sprites look like i dont know what im actually doing but trust the process...
    for num in range(1, 2):
        image_path = path + str(num) + '.png'
        pygame.image.load(image_path)
        image_list.append(pygame.image.load(image_path))
    
    return image_list

animations = {
    'playerfront' : load_anim('playerfront'),
    'playerback' : load_anim('playerback'),
    'playerright' : load_anim('playerright'),
    'playerleft' : load_anim('playerleft')
}