import pygame
import ui
import objects as ob

pygame.init()

WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
test_object = ob.Object(200, 10, 10,10, 10, (255,255,255),0,0)
running = True

while running:
    dt = clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((30, 30, 30))
    ui.draw_floor(screen)
    test_object.draw_object(screen)
    test_object.gravity()
    test_object.tick()


    pygame.display.flip()

pygame.quit()
