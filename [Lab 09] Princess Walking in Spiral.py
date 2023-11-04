#Lab 09 Kris Shields ETGG1801
##I’d encourage you to look at my solution to see how I made the game loop “flat” – your solution isn’t wrong, but there’s a lot of repeated code – if you ever find yourself doing that, there might be a cleaner way to do it.
##8/8: get player to move and change frames
##8/8: Make player change direction after reaching the end of a “segment” [4] and increase segment size [4]
##5/5: End the game when the player goes off-screen [3], and show a “game over” message [2]
##4/4: Leave a trail behind the player
##3/4: Draw all the main variables on-screen
##Drawing each line separately would make the output a bit easier to read (mostly because as the numbers change, the text after it “jitters” a bit)
8/+8: Collectible that respawns when the player touches it.
#import modules
import pygame
pygame.init()
import random
import time
import math
#draw pygame window
win_x = 800
win_y = 600
win_dim = (win_x,win_y)
win = pygame.display.set_mode(win_dim)
#load assets
wood = pygame.image.load("Images\Wood.jpg")
princess = pygame.image.load("Images\Princess.jpg")
#draw objects
win.blit(wood,(0,0))
game_over = False
princess_size = 96
movement_direction = 0
princess_frame = 0
princess_step_count = 0
princess_step_max = 1
coin_x = random.randint(1,800)
coin_y = random.randint(1,600)
coin_pos =(coin_x,coin_y)
coin_collect = 0
#define extra variables for trail:
circle_size = 5
circle_x = (((win_x/2)))
circle_y = (((win_y/2)))
circle_pos = (circle_x,circle_y)
color = (48,101,70)
#blit initial princess
win.blit(princess,(((win_x/2)-(princess_size/2)),((win_y/2)-(princess_size/2))),(princess_frame*96,movement_direction*96,princess_size,princess_size))
princess_x = (((win_x/2)-(princess_size/2)))
princess_y = (((win_y/2)-(princess_size/2)))
#set up text to display
font_obj = pygame.font.Font("Fonts/Roboto-Thin.ttf",14)
temp_surface = font_obj.render(f"Player X: {int(princess_x+princess_size/2)}, Player Y: {int(princess_y+princess_size/2)}, Current Movement Direction: {movement_direction}, Current Animation Frame: {princess_frame}, Current Steps: {princess_step_count} / {princess_step_max}, Collectibles: {coin_collect}",False,((255,255,0)))
win.blit(temp_surface,(0,0))
pygame.display.flip()
#main gameloop to cycle movement directions
while game_over == False:
    if movement_direction == 0:
        while princess_step_count < princess_step_max:
            princess_x +=5
            win.blit(wood,(0,0))
            win.blit(princess,(princess_x-48,princess_y-48),(princess_frame*96,movement_direction*96,princess_size,princess_size))
            pygame.draw.circle(win,(255,255,0),coin_pos,10)
            pygame.draw.circle(win,color,(princess_x,princess_y), circle_size)
            pygame.draw.circle(wood,color,(princess_x,princess_y), circle_size)
            #redefine variables
            x_dif = abs(princess_x - coin_x)
            y_dif = abs(princess_y - coin_y)
            hypot = math.sqrt((x_dif*x_dif)+(y_dif*y_dif))
            if hypot <=25:
                coin_collect +=1
                coin_x = random.randint(1,800)
                coin_y = random.randint(1,600)
                coin_pos =(coin_x,coin_y)
            princess_step_count +=1
            princess_frame +=1
            temp_surface = font_obj.render(f"Player X: {int(princess_x+princess_size/2)}, Player Y: {int(princess_y+princess_size/2)}, Current Movement Direction: {movement_direction}, Current Animation Frame: {princess_frame}, Current Steps: {princess_step_count} / {princess_step_max}, Collectibles: {coin_collect}",False,((255,255,0)))
            win.blit(temp_surface,(0,0))
            pygame.display.flip()
            time.sleep(.03)
            if princess_frame ==8:
                princess_frame = 0
        movement_direction += 1
        princess_step_count = 0
        princess_step_max +=1
    if movement_direction == 1:
        while princess_step_count < princess_step_max:
            princess_x +=5
            princess_y -=5
            win.blit(wood,(0,0))
            win.blit(princess,(princess_x-48,princess_y-48),(princess_frame*96,movement_direction*96,princess_size,princess_size))
            pygame.draw.circle(win,(255,255,0),coin_pos,10)
            pygame.draw.circle(win,color,(princess_x,princess_y), circle_size)
            pygame.draw.circle(wood,color,(princess_x,princess_y), circle_size)
            #redefine variables
            x_dif = abs(princess_x - coin_x)
            y_dif = abs(princess_y - coin_y)
            hypot = math.sqrt((x_dif*x_dif)+(y_dif*y_dif))
            if hypot <=25:
                coin_collect +=1
                coin_x = random.randint(1,800)
                coin_y = random.randint(1,600)
                coin_pos =(coin_x,coin_y)
            princess_step_count +=1
            princess_frame +=1
            temp_surface = font_obj.render(f"Player X: {int(princess_x+princess_size/2)}, Player Y: {int(princess_y+princess_size/2)}, Current Movement Direction: {movement_direction}, Current Animation Frame: {princess_frame}, Current Steps: {princess_step_count} / {princess_step_max}, Collectibles: {coin_collect}",False,((255,255,0)))
            win.blit(temp_surface,(0,0))
            pygame.display.flip()
            time.sleep(.03)
            if princess_frame ==8:
                princess_frame = 0
        movement_direction += 1
        princess_step_count = 0
        princess_step_max +=1
    if movement_direction == 2:
        while princess_step_count < princess_step_max:
            princess_y -=5
            win.blit(wood,(0,0))
            win.blit(princess,(princess_x-48,princess_y-48),(princess_frame*96,movement_direction*96,princess_size,princess_size))
            pygame.draw.circle(win,(255,255,0),coin_pos,10)
            pygame.draw.circle(win,color,(princess_x,princess_y), circle_size)
            pygame.draw.circle(wood,color,(princess_x,princess_y), circle_size)
            #redefine variables
            x_dif = abs(princess_x - coin_x)
            y_dif = abs(princess_y - coin_y)
            hypot = math.sqrt((x_dif*x_dif)+(y_dif*y_dif))
            if hypot <=25:
                coin_collect +=1
                coin_x = random.randint(1,800)
                coin_y = random.randint(1,600)
                coin_pos =(coin_x,coin_y)
            princess_step_count +=1
            princess_frame +=1
            temp_surface = font_obj.render(f"Player X: {int(princess_x+princess_size/2)}, Player Y: {int(princess_y+princess_size/2)}, Current Movement Direction: {movement_direction}, Current Animation Frame: {princess_frame}, Current Steps: {princess_step_count} / {princess_step_max}, Collectibles: {coin_collect}",False,((255,255,0)))
            win.blit(temp_surface,(0,0))
            pygame.display.flip()
            time.sleep(.03)
            if princess_frame ==8:
                princess_frame = 0
        movement_direction += 1
        princess_step_count = 0
        princess_step_max +=1
    if movement_direction == 3:
        while princess_step_count < princess_step_max:
            princess_x -=5
            princess_y -=5
            win.blit(wood,(0,0))
            win.blit(princess,(princess_x-48,princess_y-48),(princess_frame*96,movement_direction*96,princess_size,princess_size))
            pygame.draw.circle(win,(255,255,0),coin_pos,10)
            pygame.draw.circle(win,color,(princess_x,princess_y), circle_size)
            pygame.draw.circle(wood,color,(princess_x,princess_y), circle_size)
            #redefine variables
            x_dif = abs(princess_x - coin_x)
            y_dif = abs(princess_y - coin_y)
            hypot = math.sqrt((x_dif*x_dif)+(y_dif*y_dif))
            if hypot <=25:
                coin_collect +=1
                coin_x = random.randint(1,800)
                coin_y = random.randint(1,600)
                coin_pos =(coin_x,coin_y)
            princess_step_count +=1
            princess_frame +=1
            temp_surface = font_obj.render(f"Player X: {int(princess_x+princess_size/2)}, Player Y: {int(princess_y+princess_size/2)}, Current Movement Direction: {movement_direction}, Current Animation Frame: {princess_frame}, Current Steps: {princess_step_count} / {princess_step_max}, Collectibles: {coin_collect}",False,((255,255,0)))
            win.blit(temp_surface,(0,0))
            pygame.display.flip()
            time.sleep(.03)
            if princess_frame ==8:
                princess_frame = 0
        movement_direction += 1
        princess_step_count = 0
        princess_step_max +=1
    if movement_direction == 4:
        while princess_step_count < princess_step_max:
            princess_x -=5
            win.blit(wood,(0,0))
            win.blit(princess,(princess_x-48,princess_y-48),(princess_frame*96,movement_direction*96,princess_size,princess_size))
            pygame.draw.circle(win,(255,255,0),coin_pos,10)
            pygame.draw.circle(win,color,(princess_x,princess_y), circle_size)
            pygame.draw.circle(wood,color,(princess_x,princess_y), circle_size)
            #redefine variables
            x_dif = abs(princess_x - coin_x)
            y_dif = abs(princess_y - coin_y)
            hypot = math.sqrt((x_dif*x_dif)+(y_dif*y_dif))
            if hypot <=25:
                coin_collect +=1
                coin_x = random.randint(1,800)
                coin_y = random.randint(1,600)
                coin_pos =(coin_x,coin_y)
            princess_step_count +=1
            princess_frame +=1
            temp_surface = font_obj.render(f"Player X: {int(princess_x+princess_size/2)}, Player Y: {int(princess_y+princess_size/2)}, Current Movement Direction: {movement_direction}, Current Animation Frame: {princess_frame}, Current Steps: {princess_step_count} / {princess_step_max}, Collectibles: {coin_collect}",False,((255,255,0)))
            win.blit(temp_surface,(0,0))
            pygame.display.flip()
            time.sleep(.03)
            if princess_frame ==8:
                princess_frame = 0
        movement_direction += 1
        princess_step_count = 0
        princess_step_max +=1
    if movement_direction == 5:
        while princess_step_count < princess_step_max:
            princess_x -=5
            princess_y +=5
            win.blit(wood,(0,0))
            win.blit(princess,(princess_x-48,princess_y-48),(princess_frame*96,movement_direction*96,princess_size,princess_size))
            pygame.draw.circle(win,(255,255,0),coin_pos,10)
            pygame.draw.circle(win,color,(princess_x,princess_y), circle_size)
            pygame.draw.circle(wood,color,(princess_x,princess_y), circle_size)
            #redefine variables
            x_dif = abs(princess_x - coin_x)
            y_dif = abs(princess_y - coin_y)
            hypot = math.sqrt((x_dif*x_dif)+(y_dif*y_dif))
            if hypot <=25:
                coin_collect +=1
                coin_x = random.randint(1,800)
                coin_y = random.randint(1,600)
                coin_pos =(coin_x,coin_y)
            princess_step_count +=1
            princess_frame +=1
            temp_surface = font_obj.render(f"Player X: {int(princess_x+princess_size/2)}, Player Y: {int(princess_y+princess_size/2)}, Current Movement Direction: {movement_direction}, Current Animation Frame: {princess_frame}, Current Steps: {princess_step_count} / {princess_step_max}, Collectibles: {coin_collect}",False,((255,255,0)))
            win.blit(temp_surface,(0,0))
            pygame.display.flip()
            time.sleep(.03)
            if princess_frame ==8:
                princess_frame = 0
        movement_direction += 1
        princess_step_count = 0
        princess_step_max +=1
    if movement_direction == 6:
        while princess_step_count < princess_step_max:
            princess_y +=5
            win.blit(wood,(0,0))
            win.blit(princess,(princess_x-48,princess_y-48),(princess_frame*96,movement_direction*96,princess_size,princess_size))
            pygame.draw.circle(win,(255,255,0),coin_pos,10)
            pygame.draw.circle(win,color,(princess_x,princess_y), circle_size)
            pygame.draw.circle(wood,color,(princess_x,princess_y), circle_size)
            #redefine variables
            x_dif = abs(princess_x - coin_x)
            y_dif = abs(princess_y - coin_y)
            hypot = math.sqrt((x_dif*x_dif)+(y_dif*y_dif))
            if hypot <=25:
                coin_collect +=1
                coin_x = random.randint(1,800)
                coin_y = random.randint(1,600)
                coin_pos =(coin_x,coin_y)
            princess_step_count +=1
            princess_frame +=1
            temp_surface = font_obj.render(f"Player X: {int(princess_x+princess_size/2)}, Player Y: {int(princess_y+princess_size/2)}, Current Movement Direction: {movement_direction}, Current Animation Frame: {princess_frame}, Current Steps: {princess_step_count} / {princess_step_max}, Collectibles: {coin_collect}",False,((255,255,0)))
            win.blit(temp_surface,(0,0))
            pygame.display.flip()
            time.sleep(.03)
            if princess_frame ==8:
                princess_frame = 0
        movement_direction += 1
        princess_step_count = 0
        princess_step_max +=1
    if movement_direction == 7:
        while princess_step_count < princess_step_max:
            princess_x +=5
            princess_y +=5
            win.blit(wood,(0,0))
            win.blit(princess,(princess_x-48,princess_y-48),(princess_frame*96,movement_direction*96,princess_size,princess_size))
            pygame.draw.circle(win,(255,255,0),coin_pos,10)
            pygame.draw.circle(win,color,(princess_x,princess_y), circle_size)
            pygame.draw.circle(wood,color,(princess_x,princess_y), circle_size)
            #redefine variables
            x_dif = abs(princess_x - coin_x)
            y_dif = abs(princess_y - coin_y)
            hypot = math.sqrt((x_dif*x_dif)+(y_dif*y_dif))
            if hypot <=25:
                coin_collect +=1
                coin_x = random.randint(1,800)
                coin_y = random.randint(1,600)
                coin_pos =(coin_x,coin_y)
            princess_step_count +=1
            princess_frame +=1
            temp_surface = font_obj.render(f"Player X: {int(princess_x+princess_size/2)}, Player Y: {int(princess_y+princess_size/2)}, Current Movement Direction: {movement_direction}, Current Animation Frame: {princess_frame}, Current Steps: {princess_step_count} / {princess_step_max}, Collectibles: {coin_collect}",False,((255,255,0)))
            win.blit(temp_surface,(0,0))
            pygame.display.flip()
            time.sleep(.03)
            if princess_frame ==8:
                princess_frame = 0
        movement_direction += 1
        princess_step_count = 0
        princess_step_max +=1
    if movement_direction ==8:
        movement_direction = 0
    if(princess_y>=650):
      game_over = True
#gameover in middle
GO_surface = font_obj.render("Game Over",False,((255,255,0)))
win.blit(GO_surface,(400,300))
pygame.display.flip()
time.sleep(3)
pygame.quit()