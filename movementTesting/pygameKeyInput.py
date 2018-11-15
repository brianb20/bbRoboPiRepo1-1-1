import pygame
import sys
import time

l1 = True
posX = 0
posZ = 0

pygame.init()

move_ticker = 0
while l1 == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #keys = pygame.key.get_pressed()
            #if keys[pygame.K_w]:
            if event.key == pygame.K_w:
                print("HELLO THERE!")
                if move_ticker == 0:
                    move_ticker = 10
                    posX += 1
            #if keys[pygame.K_s]:
            if event.key == pygame.K_s:
                if move_ticker == 0:
                    move_ticker = 10
                    posX -= 1
            #if keys[pygame.K_a]:
            if event.key == pygame.K_a:
                if move_ticker == 0:
                    move_ticker = 10
                    posZ -= 1
            #if keys[pygame.K_d]:
            if event.key == pygame.K_d:
                if move_ticker == 0:
                    move_ticker = 10
                    posZ += 1
            print("POSITION X: " + str(posX) + " Z: " + str(posZ))
            if posX > 100 or posZ > 100:
                break
            if move_ticker > 0:
                move_ticker -= 1
            print ("Move Ticker: " + str(move_ticker))
