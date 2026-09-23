import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("手动操控方块动画")
clock = pygame.time.Clock()  #提前建好clock

x,y = 400,300
speed = 5
font = pygame.font.Font("C:/Windows/Fonts/msyh.ttc", 36)  #建字体文件 36字号

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()  #看当前所有键的状态 是否按着
    if keys[pygame.K_LEFT]:  #如果按着 就执行x -= speed
        x -= speed
    if keys[pygame.K_RIGHT]:  #event只能单次触发 pressed按住连续移动
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    x = max(0,min(750,x))  #取x和750中较小的 取0和后面的中较大的
    y = max(0,min(550,y))  #限制0<=x<=750 0<=y<=550

    screen.fill((30,30,30))  #深灰色
    
    pygame.draw.rect(screen,(0,200,200),(x,y,50,50))

    #把文字渲染成图像存到text1 x,y嵌入字符串 true抗锯齿 白色字
    text1 = font.render(f"方块位置:({x},{y})",True,(255,255,255))
    screen.blit(text1,(20,20))  #blit贴图像（文章渲染后）draw画几何图形
    
    text2 = font.render("按方向键移动 | 按 ESC 退出",True,(200,200,200))
    screen.blit(text2,(20,60))
    
    if x>700 and y<100:  #到达高地判断
        text3 = font.render("你到达了高地!",True,(255,255,0))
        screen.blit(text3,(300,300))


    pygame.display.update()
    clock.tick(60)


    
