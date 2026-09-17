import pygame
import sys


pygame.init()


screen = pygame.display.set_mode((1200, 800))
                                 
pygame.display.set_caption("我的第一个动画！")


x = 400  
y = 300  
speed_x =15
speed_y =6


blue = (0, 0, 255)
red = (0, 100, 100 )


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    x = x + speed_x
    y = y + speed_y

    
    if x > 750 or x < 0:   
        speed_x = -speed_x
    if y > 550 or y < 0:   
        speed_y = -speed_y

    
    screen.fill((0, 0, 0))
    
    pygame.draw.rect(screen, red, (x, y , 50 , 50))
    
    
    pygame.display.update()
    
    
    pygame.time.Clock().tick(60)
