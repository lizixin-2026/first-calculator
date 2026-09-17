import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("实时交互:文字+动画合体")
clock = pygame.time.Clock()

x,y = 400,300
speed = 5
font = pygame.font.Font("C:/Windows/Fonts/msyh.ttc", 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    x = max(0,min(750,x))
    y = max(0,min(550,y))

    screen.fill((30,30,30))
    
    pygame.draw.rect(screen,(0,200,200),(x,y,50,50))

    text1 = font.render(f"方块位置:({x},{y})",True,(255,255,255))
    screen.blit(text1,(20,20))
    
    text2 = font.render("按方向键移动 | 按 ESC 退出",True,(200,200,200))
    screen.blit(text2,(20,60))
    
    if x>700 and y<100:
        text3 = font.render("你到达了高地!",True,(255,255,0))
        screen.blit(text3,(300,300))


    pygame.display.update()
    clock.tick(60)


    
