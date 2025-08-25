import pygame

pygame.init()
pygame.mixer.init()

screen_w,screen_h = 800, 600
screen = pygame.display.set_mode((screen_w, screen_h))

# image load
play_button = pygame.image.load("assets/play.png").convert_alpha()
play_button = pygame.transform.scale(play_button, (90, 80))  # Scale the image to desired size

running = True
while running:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((250, 238, 238))  # Fill the screen with black
    
    screen.blit(play_button, (100, 100))
    
    pygame.display.flip()   # Update the full display Surface to the screen
pygame.quit()