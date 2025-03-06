"""
    PROJECT NAME HERE
    PROJECT DESCRIPTION HERE
    Authors: Evan Bartkowski
"""

import pygame
from pygame.locals import *
import sys
import os
import math
import random
import cv2
pygame.init()
pygame.mixer.init()
import json
import string
########################################################################################################################
########################################################################################################################
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
########################################################################################################################
########################################################################################################################
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHTBLUE = (102, 255, 255)
PURPLE = (127, 0, 255)
LIGHTGREEN = (102, 255, 180)
PINK = (255, 153, 255)
GREY = (192, 192, 192)
YELLOW = (255, 255, 51)
DARKGREEN = (51, 102, 0)
GOLD = (255, 197, 46)
SKYBLUE = (204, 255, 255)
TAN = (245, 197, 135)
DARKRED = (108, 5, 5)
DARKPURPLE = (130,20,255)
AQUA = (0, 247, 255)
EMERALD = (67, 192, 148)
ORANGEDESERT = (241, 99, 1)
LIGHTYELLOW = (255, 255, 153)
SWAMPGREEN = (0, 51, 0)
DARKGEMBLUE = (0, 0, 51)
VELVET = (102, 0, 51)
LIME = (102, 255, 102)
PINPPINK = (255, 102, 102)
MURKY = (51, 51, 0)
CLOUD = (204, 229, 255)
SLEEPPURPLE = (204, 153, 255)

displaylength = 1920
displayheight = 1080
halfdisplay = displaylength / 2
DISPLAYSURF = pygame.display.set_mode((displaylength, displayheight))
DISPLAYSURF.fill(WHITE)

pygame.display.set_caption("Game")
font = pygame.font.SysFont(None, 75)
font2 = pygame.font.SysFont("Arial", 60)
font3 = pygame.font.SysFont("Times New Roman", 40)
font4 = pygame.font.SysFont("Comic Sans", 40)
font5 = pygame.font.SysFont("Comic Sans", 20)
font6 = pygame.font.Font(resource_path("fonts/Danger.otf"), 25)
font7 = pygame.font.Font(resource_path("fonts/eroded.ttf"), 20)
font8 = pygame.font.Font(resource_path("fonts/HelpMe.ttf"), 20)
font9 = pygame.font.Font(resource_path("fonts/Overwave.otf"), 20)
font10 = pygame.font.Font(resource_path("fonts/Comfy.otf"), 22)
font11 = pygame.font.Font(resource_path("fonts/anime.otf"), 15)
font12 = pygame.font.Font(resource_path("fonts/oldenFont.otf"), 50)
font13 = pygame.font.Font(resource_path("fonts/SwordsmanFont.TTF"), 20)
font14 = pygame.font.Font(resource_path("fonts/AsianFont.ttf"), 20)
font15 = pygame.font.Font(resource_path("fonts/womenfont.ttf"), 20)
font16 = pygame.font.Font(resource_path("fonts/runefont.otf"), 50)
font17 = pygame.font.Font(resource_path("fonts/dragonfont.ttf"), 20)
font18 = pygame.font.Font(resource_path("fonts/oldenFont.otf"), 70)
font19 = pygame.font.Font(resource_path("fonts/Danger.otf"), 100)
font20 = pygame.font.Font(resource_path("fonts/AsianFont.ttf"), 60)
font21 = pygame.font.SysFont("Comic Sans", 16)
font22 = pygame.font.Font(resource_path("fonts/AsianFont.ttf"), 50)
font23 = pygame.font.Font(resource_path("fonts/oldenFont.otf"), 35)
font24 = pygame.font.Font(resource_path("fonts/AsianFont.ttf"), 40)
font25 = pygame.font.SysFont("Comic Sans", 30)
font26 = pygame.font.Font(resource_path("fonts/AsianFont.ttf"), 30)

startimage = pygame.image.load(resource_path('images/godspireimage.webp'))
startimage = pygame.transform.scale(startimage, (1550, 870))
blackscreenimage = pygame.image.load(resource_path('images/blackscreen.jpg'))
blackscreenimage = pygame.transform.scale(blackscreenimage, (3000, 3000))
blueglowimage = pygame.image.load(resource_path('images/blueglow.png'))
blueglowimage = pygame.transform.scale(blueglowimage, (100, 100))
characterchooseimage = pygame.image.load(resource_path('images/characterchoose.jpg'))
characterchooseimage = pygame.transform.scale(characterchooseimage, (1550, 870))
emptycharacterimage = pygame.image.load(resource_path('images/emptycharacter.png'))
mapscreenimage = pygame.image.load(resource_path('images/mapscreenimage.webp'))
mapscreenimage = pygame.transform.scale(mapscreenimage, (1550, 870))
map1image = pygame.image.load(resource_path('images/map1.webp'))
map1image = pygame.transform.scale(map1image, (1550, 870))
startvideo = cv2.VideoCapture(resource_path("video/goldglitterbackground.mp4"))

########################################################################################################################
def draw_text(text, font, color, surface, x, y, alpha=255):
    textobj = font.render(text, True, color)  # Render the text
    textobj.set_alpha(alpha)  # Set the alpha for transparency
    textrect = textobj.get_rect()  # Create a rectangle for the text
    textrect.topleft = (x, y)  # Set the position of the text
    surface.blit(textobj, textrect)  # Blit the text surface onto the display surface
########################################################################################################################
def draw_text_center(text, font, color, surface, x, y, alpha=255):
    textobj = font.render(text, True, color)  # Render the text
    textobj.set_alpha(alpha)  # Set the alpha for transparency
    textrect = textobj.get_rect()  # Create a rectangle for the text
    textrect.midtop = (x, y)  # Center the rectangle at the specified position
    surface.blit(textobj, textrect)  # Blit the text surface onto the display surfac
########################################################################################################################
def transition(speed):
    transitionbool = True
    transitioncounter = 1
    while (transitionbool == True):
        transitioncounter = transitioncounter + speed
        blackscreenimage.set_alpha(transitioncounter)
        DISPLAYSURF.blit(blackscreenimage, (0, 0))
        pygame.display.update()
        if (transitioncounter >= 240):
            transitionbool = False
            transitioncounter = 1
########################################################################################################################
class StartMenu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.menu_active = True
    def StartupScreen(self):

        pygame.mixer.music.load(resource_path("audio/nocturnal.mp3"))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        while self.menu_active:
            startTime = pygame.time.get_ticks()
            DISPLAYSURF.fill(WHITE)
            DISPLAYSURF.blit(startimage, (191, 105))
            rainbowcolor1 = int((math.sin(startTime * 0.002) + 1) * 127.5)
            rainbowcolor2 = int((math.sin(startTime * 0.003 + 2) + 1) * 127.5)
            rainbowcolor3 = int((math.sin(startTime * 0.004 + 2) + 1) * 127.5)

            mouseX, mouseY = pygame.mouse.get_pos()
            mouse_pos = pygame.mouse.get_pos()


            ret, frame = startvideo.read()
            if not ret:
                startvideo.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue  # Continue to the next loop iteration
            frame = cv2.resize(frame, (1550, 880))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_surface = pygame.surfarray.make_surface(frame)
            frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
            frame_surface = pygame.transform.flip(frame_surface, True, False)
            frame_surface.set_alpha(70)
            DISPLAYSURF.blit(frame_surface, (190, 100))


                # Display the Start Menu options
            rect_position = (DISPLAYSURF.get_width() - 40, 10, 50, 50)
            pygame.draw.rect(DISPLAYSURF, WHITE, rect_position)
            draw_text_center('kpasvmjioewnacvxcxvsdskdsmdkasdxc', font16, (220, 20, rainbowcolor1), DISPLAYSURF, halfdisplay, 125, 200)
            draw_text_center('[ Click to enter the Spire ]', font18, (rainbowcolor1, rainbowcolor2, rainbowcolor3), DISPLAYSURF, halfdisplay, 300)
            draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
            if 1680 <= mouse_pos[0] <= 1920 and 0 <= mouse_pos[1] <= 155:
                draw_text('x', font4, (rainbowcolor2,rainbowcolor3, rainbowcolor1), DISPLAYSURF,1685, 105)

            mouseX, mouseY = pygame.mouse.get_pos()
            blueglowimage.set_alpha(140)
            DISPLAYSURF.blit(blueglowimage, (mouseX - 47, mouseY - 44))
            for event in pygame.event.get():
                mouseX, mouseY = pygame.mouse.get_pos()
                blueglowimage.set_alpha(140)
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    if 1680 <= mouseX <= 1920 and 0 <= mouseY <= 155:
                        print("Quit clicked")
                        pygame.mixer.music.stop()  # Stop the music when quitting
                        pygame.quit()
                        sys.exit()
                    else:
                        startvideo.release()
                        transition(6)
                        maingameareas()

            pygame.display.update()
########################################################################################################################
class maingameareas(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.characterscreen()
        self.mapscreen()
        self.battle()
########################################################################################################################
    def characterscreen(self):
        pygame.mixer.music.load(resource_path("audio/fantasy1.mp3"))
        pygame.mixer.music.queue(resource_path("audio/fantasy2.mp3"))
        pygame.mixer.music.play(-1)
        mainloop = True
        video = cv2.VideoCapture(resource_path("video/battlebackground.mp4"))


        while(mainloop):

            startTime = pygame.time.get_ticks()
            rainbowcolor1 = int((math.sin(startTime * 0.002) + 1) * 127.5)
            rainbowcolor2 = int((math.sin(startTime * 0.003 + 2) + 1) * 127.5)
            rainbowcolor3 = int((math.sin(startTime * 0.004 + 2) + 1) * 127.5)

            mouseX, mouseY = pygame.mouse.get_pos()
            mouse_pos = pygame.mouse.get_pos()
            DISPLAYSURF.fill(BLACK)
            DISPLAYSURF.blit(characterchooseimage, (195, 100))

            character1rect = pygame.Rect(658, 266, 100, 90)

            rainbow = (rainbowcolor1,rainbowcolor2,rainbowcolor3)

            ret, frame = video.read()
            if not ret:
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue  # Continue to the next loop iteration
            frame = cv2.resize(frame, (1550, 880))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_surface = pygame.surfarray.make_surface(frame)
            frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
            frame_surface = pygame.transform.flip(frame_surface, True, False)
            frame_surface.set_alpha(70)
            DISPLAYSURF.blit(frame_surface, (190, 100))

            draw_text("Character1", font13, GREEN, DISPLAYSURF, 658, 220)
            DISPLAYSURF.blit(emptycharacterimage, (688, 266))

            if character1rect.collidepoint(mouse_pos):
                draw_text("Character1", font13, rainbow, DISPLAYSURF, 658, 220)
                pygame.draw.rect(DISPLAYSURF, rainbow, character1rect, 5)


            blueglowimage.set_alpha(150)
            DISPLAYSURF.blit(blueglowimage, (mouseX - 47, mouseY - 44))



            mouseX, mouseY = pygame.mouse.get_pos()
            print("x and y = " +str(mouseX) +" " +str(mouseY))


            draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
            xrect = pygame.Rect(1680, 123, 35, 35)
            if xrect.collidepoint(mouse_pos):
                draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)

            for event in pygame.event.get():

                if event.type == MOUSEBUTTONDOWN:
                    if character1rect.collidepoint(mouse_pos):
                        transition(6)
                        mainloop = False
                    if xrect.collidepoint(mouse_pos):
                        print("Quit clicked")
                        video.release()
                        pygame.mixer.music.stop()
                        mainloop = False
                        pygame.quit()
                        sys.exit()
            pygame.display.update()
########################################################################################################################
########################################################################################################################
    def mapscreen(self):
        mainloop = True
        video = cv2.VideoCapture(resource_path("video/battlebackground.mp4"))

        while(mainloop):

            startTime = pygame.time.get_ticks()
            rainbowcolor1 = int((math.sin(startTime * 0.002) + 1) * 127.5)
            rainbowcolor2 = int((math.sin(startTime * 0.003 + 2) + 1) * 127.5)
            rainbowcolor3 = int((math.sin(startTime * 0.004 + 2) + 1) * 127.5)

            mouseX, mouseY = pygame.mouse.get_pos()
            mouse_pos = pygame.mouse.get_pos()
            DISPLAYSURF.fill(BLACK)
            DISPLAYSURF.blit(mapscreenimage, (195, 100))

            map1rect = pygame.Rect(192, 108, 283, 428)
            rainbow = (rainbowcolor1,rainbowcolor2,rainbowcolor3)




            ret, frame = video.read()
            if not ret:
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue  # Continue to the next loop iteration
            frame = cv2.resize(frame, (1550, 880))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_surface = pygame.surfarray.make_surface(frame)
            frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
            frame_surface = pygame.transform.flip(frame_surface, True, False)
            frame_surface.set_alpha(70)
            DISPLAYSURF.blit(frame_surface, (190, 100))

            pygame.draw.rect(DISPLAYSURF, WHITE, map1rect, 7)

            if map1rect.collidepoint(mouse_pos):
                pygame.draw.rect(DISPLAYSURF, rainbow, map1rect, 7)

            blueglowimage.set_alpha(150)
            DISPLAYSURF.blit(blueglowimage, (mouseX - 47, mouseY - 44))



            mouseX, mouseY = pygame.mouse.get_pos()
            print("x and y = " +str(mouseX) +" " +str(mouseY))


            draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
            xrect = pygame.Rect(1680, 123, 35, 35)
            if xrect.collidepoint(mouse_pos):
                draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)

            for event in pygame.event.get():

                if event.type == MOUSEBUTTONDOWN:
                    if map1rect.collidepoint(mouse_pos):
                        transition(6)
                        mainloop = False
                    if xrect.collidepoint(mouse_pos):
                        print("Quit clicked")
                        video.release()
                        pygame.mixer.music.stop()
                        mainloop = False
                        pygame.quit()
                        sys.exit()
            pygame.display.update()
########################################################################################################################
    def battle(self):
        pygame.mixer.music.load(resource_path("audio/fantasy1.mp3"))
        pygame.mixer.music.queue(resource_path("audio/fantasy2.mp3"))
        pygame.mixer.music.play(-1)
        mainloop = True
        video = cv2.VideoCapture(resource_path("video/glowparticlevideo.mp4"))
        characterx = 0
        charactery = 0

        while(mainloop):

            startTime = pygame.time.get_ticks()
            rainbowcolor1 = int((math.sin(startTime * 0.002) + 1) * 127.5)
            rainbowcolor2 = int((math.sin(startTime * 0.003 + 2) + 1) * 127.5)
            rainbowcolor3 = int((math.sin(startTime * 0.004 + 2) + 1) * 127.5)

            mouseX, mouseY = pygame.mouse.get_pos()
            mouse_pos = pygame.mouse.get_pos()
            DISPLAYSURF.fill(BLACK)
            DISPLAYSURF.blit(map1image, (195, 100))

            characterrect = pygame.Rect(930 + characterx, 530 + charactery, 100, 90)
            rainbow = (rainbowcolor1,rainbowcolor2,rainbowcolor3)

            ret, frame = video.read()
            if not ret:
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue  # Continue to the next loop iteration
            frame = cv2.resize(frame, (1550, 880))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_surface = pygame.surfarray.make_surface(frame)
            frame_surface = pygame.transform.rotate(frame_surface, -90)  # Rotate if necessary
            frame_surface = pygame.transform.flip(frame_surface, True, False)
            frame_surface.set_alpha(50)
            DISPLAYSURF.blit(frame_surface, (190, 100))

            DISPLAYSURF.blit(emptycharacterimage, (930 + characterx, 530 + charactery))




            mouseX, mouseY = pygame.mouse.get_pos()
            print("x and y = " +str(mouseX) +" " +str(mouseY))


            draw_text('x', font4, BLACK, DISPLAYSURF, 1685, 105)
            xrect = pygame.Rect(1680, 123, 35, 35)
            if xrect.collidepoint(mouse_pos):
                draw_text('x', font4, RED, DISPLAYSURF, 1685, 105)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        charactery = charactery - 10
                    if event.key == pygame.K_s:
                        charactery = charactery + 10
                    if event.key == pygame.K_a:
                        characterx = characterx - 10
                    if event.key == pygame.K_d:
                        characterx = characterx + 10
                else:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_w]:
                        charactery = charactery - 10
                    if keys[pygame.K_s]:
                        charactery = charactery + 10
                    if keys[pygame.K_a]:
                        characterx = characterx - 10
                    if keys[pygame.K_d]:
                        characterx = characterx + 10
                if event.type == MOUSEBUTTONDOWN:
                    if xrect.collidepoint(mouse_pos):
                        print("Quit clicked")
                        video.release()
                        pygame.mixer.music.stop()
                        mainloop = False
                        pygame.quit()
                        sys.exit()
            pygame.display.update()
########################################################################################################################
#########################################################################################################################
if __name__ == "__main__":
    menu = StartMenu()
    menu.StartupScreen()
    print("Game Started")
