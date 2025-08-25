import pygame

pygame.init()
pygame.mixer.init()

screen_w,screen_h = 800, 600
screen = pygame.display.set_mode((screen_w, screen_h))

# image load
# music paly button
play_button = pygame.image.load("assets/play.png").convert_alpha()
play_button = pygame.transform.scale(play_button, (90, 80))  # Scale the image to desired size
play_button_rect = play_button.get_rect(x=100, y=100 )

# music load
loaded_music = pygame.mixer.Sound("music/test.mp3")

running = True
while running:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                loaded_music.play(-1)
            
    mos_pos = pygame.mouse.get_pos()
    screen.fill((250, 238, 238))  # Fill the screen with black
    screen.blit(play_button, play_button_rect)  
    
    
    
    
    pygame.display.flip()   # Update the full display Surface to the screen
pygame.quit()