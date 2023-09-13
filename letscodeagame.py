import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surface= test_font.render(f'Score:{current_time}',False,(64,64,64))
    # current_time is an integer heare and we want an string
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rect)
    return current_time
    
  
pygame.init()    #initializing

 #set width and height of the screen
screen = pygame.display.set_mode((800,400))   #display surface
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font=pygame.font.Font("/Users/aryansinghal/code/pygame/font/Pixeltype.ttf",50)
game_active = True
start_time = 0
score= 0
#test_surface= pygame.Surface((100,200))      # surface
#test_surface.fill("red")
#any graphical input will be a new surface
sky_surface = pygame.image.load("/Users/aryansinghal/code/pygame/graphics/sky.png").convert()
ground_surface = pygame.image.load("/Users/aryansinghal/code/pygame/graphics/ground.png").convert()
# score_surface = test_font.render("My Game", False,(64,64,64))
# score_rect = score_surface.get_rect(center=(400,50))
snail_surface = pygame.image.load("/Users/aryansinghal/code/pygame/graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600,300))
#snail_x_pos =600

player_surface = pygame.image.load("/Users/aryansinghal/code/pygame/graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80,300))
player_gravity = 0
#intro screen
player_stand = pygame.image.load("/Users/aryansinghal/code/pygame/graphics/Player/player_stand.png").convert_alpha()
player_stand = pygame.transform.scale(player_stand,(100,100))
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render("Pixel Runner", False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,70))

game_message = test_font.render("press space to run",False,(111,196,169))
game_message_rect = game_message.get_rect(center=(4  00,320))

score_message = text.font.render(f'Your Score:{score}', False ,(111,196,169))
score_message_rect = score_message.get_rect( center = (400,330))


while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:    
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300 :  #(MOUSEBUTTONDOWN,MOUSEBUTTONUP)
                if player_rect.collidepoint(event.pos):
                    player_gravity =-20
    
            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_SPACE and player_rect.bottom >= 300 :
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key== pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks()/1000) 




    if game_active:       
        screen.blit(sky_surface,(0,0))      #(surface,position)
        screen.blit(ground_surface,(0,300))

        # pygame.draw.rect(screen, "#c0e8ec", score_rect)
        # pygame.draw.rect(screen, "#c0e8ec", score_rect,10)
        
        # screen.blit(score_surface,score_rect)
        score = display_score()
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
        if player_rect.bottom >= 300 :
            player_rect.bottom = 300

        screen.blit(player_surface,player_rect)


        #collision
        if snail_rect.colliderect(player_rect):
            game_active = False


    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        
        screen.blit(game_name,game_name_rect)
        screen.blit(game_message,game_message_rect)
        if score == 0:
            screen.blit(game_message,game_message_rect)
        else:
            screen.blit(score_message,score_message_rect)




 
    pygame.display.update()              #update everything
    clock.tick(60)



