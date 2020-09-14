import time
import pygame
#time_string = time.strftime("%H:%M:%S")
#print(time_string)
#initilize pygame
pygame.init()

#creates the size of the screen
screen = pygame.display.set_mode((610, 410))

#variables
#real_time = time.strftime("%H  %M  %S")
font = pygame.font.Font('freesansbold.ttf', 70)
textX = 40
textY = 150


def show_time(x, y):
    time_display = font.render("Time: "+str(real_time), True, (255, 255, 255))
    screen.blit(time_display, (x, y))


#background
background = pygame.image.load("space.jpeg")

#title and icon
pygame.display.set_caption("Digital Clock")
icon = pygame.image.load("wake-up.png")
pygame.display.set_icon(icon)

running = True
while running:
    real_time = time.strftime("%H  %M  %S")
    #print(real_time)

    screen.fill((0, 0, 0))

    #load background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    show_time(textX, textY)
    pygame.display.update()
