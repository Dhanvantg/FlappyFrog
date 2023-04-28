import pygame
import os

pygame.font.init()
pygame.mixer.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
pygame.display.set_caption("Flappy Frog")
game_state = "menu"
bg = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bg.png")), (width, height))

# Colors
grey = (46, 46, 46)
cyan = (27, 177, 194)

def menu():
    screen.blit(bg, (0, 0))
    font = pygame.font.SysFont('arial', 40)

    # Title
    title = pygame.transform.scale(pygame.image.load("assets\\title.png").convert_alpha(), (width//2, width*3 // 28))
    #title = pygame.transform.scale(title)
    titlepos = width//2 - title.get_width()//2, title.get_height() // 2
    screen.blit(title, (width//2 - title.get_width()//2, title.get_height() // 2))

    # Buttons
    b1pos = width // 2 - width // 12, height // 3 + titlepos[1]
    pygame.draw.rect(screen, grey, [width // 2 - width // 12, height // 3 + titlepos[1], width // 6, height // 12], 0, 15)
    b1text = font.render('MENU', True, cyan)
    screen.blit(b1text, (b1pos[0] - b1text.get_width() // 2 + width // 12, b1pos[1] + b1text.get_height() // 2))
    pygame.draw.rect(screen, cyan, [width // 2 - width // 12, height // 3 + titlepos[1], width // 6, height // 12], 5, 15)

    b2pos = width // 2 - width // 12, height // 6 + b1pos[1]
    pygame.draw.rect(screen, grey, [width // 2 - width // 12, height // 6 + b1pos[1], width // 6, height // 12], 0, 15)
    b2text = font.render('CUSTOMIZE', True, cyan)
    screen.blit(b2text, (b2pos[0] - b2text.get_width() // 2 + width // 12, b2pos[1] + b2text.get_height() // 2))
    pygame.draw.rect(screen, cyan, [width // 2 - width // 12, height // 6 + b1pos[1], width // 6, height // 12], 5, 15)

    # Frog
    frog = pygame.transform.scale(pygame.image.load(os.path.join("assets", "frog-green.png")), (height//3, height//3))
    screen.blit(frog, (width*2//3 + frog.get_width() // 2, height - frog.get_height()*11//10))

    pygame.display.flip()

while True:

    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()
    if game_state == "menu":
        menu()
