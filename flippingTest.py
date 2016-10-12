'''
Created on Dec 18, 2014

@author: justin
'''
import sys, pygame
pygame.init()

screen = pygame.display.set_mode([1000, 600])
screen.fill([255, 255, 255])

class Fish(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.center = location

fish = Fish("fish1.png", [500, 300])

fish.image = pygame.transform.flip(fish.image, True, False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
                
    screen.blit(fish.image, fish.rect)
    pygame.display.flip()