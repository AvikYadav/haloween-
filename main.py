from time import sleep
import pygame
pygame.init()

widow = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load('ratsasan.mp3')
pygame.mixer.music.play()
sleep(6)
pygame.mixer.music.load('scary.mp3')
pygame.mixer.music.play()

for i in range(6):
    image = pygame.image.load('scr.jpg')
    widow.blit(image, (0, 0))
    pygame.display.update()
    sleep(0.2)
    image2 = pygame.image.load("backScreen.jpg")
    widow.blit(image2, (0, 0))
    pygame.display.update()
    sleep(0.2)

