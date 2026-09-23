import pygame  #拿出pygame游戏库（做图形 动画 游戏）
import sys  #拿出sys模块（用来退出程序）


pygame.init()  #唤醒pygame功能“开机”


screen = pygame.display.set_mode((1200, 800))  #显示模块+窗口大小设置
                                 
pygame.display.set_caption("第一个方块动画")  #显示模块+窗口标题设置


x = 400  #定义方块初始位置（左上角为坐标原点）  
y = 300  
speed_x =15  #定义方块速度（像素/帧）
speed_y =6


blue = (0, 0, 255)  #python颜色（R,G,B）（0，0，0）黑 （255，255，255）白
cyan = (0, 100, 100)


while True:  #主无限循环开始
    
    for event in pygame.event.get():  #一个个检查 这一帧发生的所有事件
        if event.type == pygame.QUIT:  #如果点×
            pygame.quit()  #关闭python 释放资源
            sys.exit()  #彻底退出python

    
    x = x + speed_x  #每一帧不断变化方块坐标
    y = y + speed_y

    
    if x > 1150 or x < 0:  #碰壁反弹 速度反向   
        speed_x = -speed_x
    if y > 750 or y < 0:   
        speed_y = -speed_y

    screen.fill((255, 255, 255))  #清屏 除去上一帧画面
    
    
    pygame.draw.rect(screen, cyan, (x, y , 50 , 50))  #画方块（坐标+方块长宽） 
    
    
    pygame.display.update()  #把画好的方块放屏幕上 每一帧更新一次
    
    
    pygame.time.Clock().tick(60)  #控制帧率 创建时钟+每秒最多60帧
