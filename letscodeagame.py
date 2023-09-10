import pygame
from sys import exit
pygame.init()    #initializing

 #set width and height of the screen
screen = pygame.display.set_mode((800,400))   #display surface
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font=pygame.font.Font("/Users/aryansinghal/code/pygame/font/Pixeltype.ttf",50)

#test_surface= pygame.Surface((100,200))      # surface
#test_surface.fill("red")
#any graphical input will be a new surface
sky_surface = pygame.image.load("/Users/aryansinghal/code/pygame/graphics/sky.png").convert()
ground_surface = pygame.image.load("/Users/aryansinghal/code/pygame/graphics/ground.png").convert()

score_surface = test_font.render("My Game", False,(64,64,64))
score_rect = score_surface.get_rect(center=(400,50))

snail_surface = pygame.image.load("/Users/aryansinghal/code/pygame/graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600,300))
#snail_x_pos =600

player_surface = pygame.image.load("/Users/aryansinghal/code/pygame/graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80,300))

player_gravity = 0
while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:  #(MOUSEBUTTONDOWN,MOUSEBUTTONUP)
            if player_rect.collidepoint(event.pos):
                player_gravity =-20
 
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_SPACE:
                player_gravity = -20

           
    screen.blit(sky_surface,(0,0))      #(surface,position)
    screen.blit(ground_surface,(0,300))

    pygame.draw.rect(screen, "#c0e8ec", score_rect)
    pygame.draw.rect(screen, "#c0e8ec", score_rect,10)
    
    screen.blit(score_surface,score_rect)
    #snail_x_pos -=3
    #if snail_x_pos < -100 :
    #   snail_x_pos =800
    
    snail_rect.x -=4
    if snail_rect.right <=0:
        snail_rect.left = 800

    screen.blit(snail_surface,snail_rect)
    #player
    player_gravity +=1
    player_rect.y += player_gravity

    screen.blit(player_surface,player_rect)

    
    #if player_rect.colliderect(snail_rect):
    #    print("collision ")

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint((mouse_pos)):
    #     #print("collision")
    #     print(pygame.mouse.get_pressed())
    

    # keys = pygame.key.get_pressed()
    # if keys[pygame.k_space]:
    #     print("jump'")

 
    pygame.display.update()              #update everything
    clock.tick(60)



