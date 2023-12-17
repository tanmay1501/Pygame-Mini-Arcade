import pygame

pygame.init()


screen = pygame.display.set_mode((400,400))

def draw_point(text, pos):
    img = font.render(text, True, BLACK)
    pygame.draw.circle(screen, RED, pos, 3)
    screen.blit(img, pos)

pts = ('topleft', 'topright', 'bottomleft', 'bottomright',
        'midtop', 'midright', 'midbottom', 'midleft', 'center')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((128,128,128))
    pygame.draw.rect(screen,(0,255,255),(50, 40, 250, 80), 4)

    for pt in pts:
        draw_point(pt, eval('rect.'+pt))

    pygame.display.flip()

pygame.quit()