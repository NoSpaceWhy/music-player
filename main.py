import pygame
from tkinter.filedialog import askopenfilename
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(1)

screen_w,screen_h = 800, 600
screen = pygame.display.set_mode((screen_w, screen_h))
font = pygame.font.Font(None, 50)
pygame.display.set_caption("Music Player")

# hover text
def hover_text_func(text_name, x_cor, y_cor):
    hover_font = pygame.font.Font(None, 25)
    hover_text_name = text_name
    hover_text = hover_font.render(hover_text_name, True, (0, 0, 0))

    hover_text_rect = hover_text.get_rect(x=x_cor, y=y_cor)
    screen.blit(hover_text, hover_text_rect)
    
# * image load
# play button
play_button = pygame.image.load("assets/play.png").convert_alpha()
play_button = pygame.transform.scale(play_button, (90, 80))  # Scale the image to desired size
play_button_rect = play_button.get_rect(x=100, y=100 )

pause_button = pygame.image.load("assets/pause.png").convert_alpha()
pause_button = pygame.transform.scale(pause_button, (90, 80))  # Scale
pause_button_rect = pause_button.get_rect(x=200, y=100 )

choose_button = pygame.image.load("assets/folder.png").convert_alpha()
choose_button = pygame.transform.scale(choose_button, (90, 80))  # Scale
choose_button_rect = choose_button.get_rect(x=300, y=100 )

# * music load
music = "music/swimming by flawedMangoes.mp3"
loaded_music = pygame.mixer.Sound(music)
music = music.removesuffix('.mp3')
music = music.split("/", 1)[1]

# * text load
music_name = font.render(music, True, (0, 0, 0))
music_name_rect = music_name.get_rect( x=0, y=400)

text = font.render("Right now listening to", True, (0, 0, 0))
text_rect = text.get_rect(y=350, x=0)

running = True
while running:   
    mos_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
    

    screen.fill((250, 238, 238))  # Fill the screen with black
    screen.blit(play_button, play_button_rect)
    screen.blit(pause_button, pause_button_rect)
    
    screen.blit(music_name, music_name_rect)
    screen.blit(text, text_rect)
    screen.blit(choose_button, choose_button_rect)
    
    if play_button_rect.collidepoint(mos_pos):
        hover_text_func("Play music", 100, 200)
        if pygame.mouse.get_pressed()[0]:  # Left mouse button is pressed
            loaded_music.play(-1)
    
    if pause_button_rect.collidepoint(mos_pos):
        hover_text_func("Pause music", 200, 200)
        if pygame.mouse.get_pressed()[0]:  # Left mouse button is pressed
             loaded_music.stop()
    
    if choose_button_rect.collidepoint(mos_pos):
        hover_text_func("Choose music", 300, 200)
        if pygame.mouse.get_pressed()[0]:  # Left mouse button is pressed
            try:
                music = askopenfilename(title="select music file", filetypes=[("MP3 files", "*.mp3")])
                loaded_music = pygame.mixer.Sound(music)
                    
                print(music)
                music = music.removesuffix('.mp3')
                music = music.split("/", 1)[1]
                print(music)
                music_name = font.render(music, True, (0, 0, 0))
                music_name_rect = music_name.get_rect( x=0, y=400)
            except FileNotFoundError:
                music = "music/swimming by flawedMangoes.mp3"
                loaded_music = pygame.mixer.Sound(music)
                    
                print(music)
                music = music.removesuffix('.mp3')
                music = music.split("/", 1)[1]
                print(music)
                music_name = font.render(music, True, (0, 0, 0))
                music_name_rect = music_name.get_rect( x=0, y=400)
                    
    # print(mos_pos)        
    pygame.display.flip()   # Update the full display Surface to the screen
pygame.quit()