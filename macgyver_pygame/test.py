import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))
image = pygame.image.load("ressource/floor-tiles-20x20.png").convert_alpha()
image2 = image.subsurface(pygame.Rect(40, 0, 20, 20))
pygame_font.quit()
f = pygame_font.Font(None, 20)
s = f.render("foo", True, [0, 0, 0], [255, 255, 255])


continuer = True
while continuer:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

    screen.blit(image2, (50, 50))
        

    pygame.display.flip()

pygame.quit()