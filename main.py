import pygame


pygame.init()

sc = pygame.display.set_mode((1000, 600))
isworking = True


while isworking:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isworking = False


pygame.quit()
exit()
