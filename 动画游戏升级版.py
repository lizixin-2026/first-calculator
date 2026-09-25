import pygame
import sys
import math
import struct
import wave
import os

#用代码生成一个蜂鸣声音效文件
def create_beep(filename="beep.wav", frequency=880, duration=0.3):
    """如果 beep.wav 不存在，就用代码生成一个简单蜂鸣声"""
    if os.path.exists(filename):
        return filename

    sample_rate = 44100
    num_samples = int(sample_rate * duration)

    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)         # 单声道
        wav_file.setsampwidth(2)         # 16 位
        wav_file.setframerate(sample_rate)

        for i in range(num_samples):
            fade = 1.0 - (i / num_samples)   # 淡出，声音越来越小
            value = int(32767 * 0.5 * fade * math.sin(2 * math.pi * frequency * i / sample_rate))
            wav_file.writeframes(struct.pack('<h', value))

    return filename

# 初始化 
pygame.mixer.pre_init(44100, -16, 1, 512)   # 先设置音频参数
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("手动操控方块动画")
clock = pygame.time.Clock()

# 加载音效（失败也不影响游戏）
try:
    beep_file = create_beep()
    beep_sound = pygame.mixer.Sound(beep_file)
except Exception as e:
    print(f"音效加载失败: {e}")
    beep_sound = None

#  方块、速度、字体 
x, y = 400, 300
speed = 5
font = pygame.font.Font("C:/Windows/Fonts/msyh.ttc", 36)

#  高地范围 
GOAL_X = 700      # 高地左边界
GOAL_Y = 100      # 高地下边界

already_played = False   # 记录是否已经播放过音效

# 主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 检测键盘
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # 边界限制
    x = max(0, min(750, x))
    y = max(0, min(550, y))

    # 清屏
    screen.fill((30, 30, 30))

    #  画红色高地平台 
    # 高地范围：右上角 (700, 0) 到 (800, 100)
    # 1. 半透明红色填充
    highland = pygame.Surface((800 - GOAL_X, GOAL_Y), pygame.SRCALPHA)
    highland.fill((255, 0, 0, 60))          # 半透明红
    screen.blit(highland, (GOAL_X, 0))

    # 2. 红色边框
    pygame.draw.rect(screen, (255, 0, 0), (GOAL_X, 0, 800 - GOAL_X, GOAL_Y), 3)

    # 3. 边界线
    pygame.draw.line(screen, (255, 0, 0), (GOAL_X, GOAL_Y), (800, GOAL_Y), 2)
    pygame.draw.line(screen, (255, 0, 0), (GOAL_X, 0), (GOAL_X, GOAL_Y), 2)

    # 画方块 
    pygame.draw.rect(screen, (0, 200, 200), (x, y, 50, 50))

    #  显示文字 
    text1 = font.render(f"方块位置:({x},{y})", True, (255, 255, 255))
    screen.blit(text1, (20, 20))

    text2 = font.render("按方向键移动 | 红色区域为高地", True, (200, 200, 200))
    screen.blit(text2, (20, 60))

    #  到达高地判断 
    if x > GOAL_X and y < GOAL_Y:
        text3 = font.render("你到达了高地!", True, (255, 255, 0))
        screen.blit(text3, (300, 300))

        # 播放音效（只播一次）
        if not already_played and beep_sound:
            beep_sound.play()
            already_played = True
    else:
        already_played = False   # 离开高地后，下次到达可以再播

    pygame.display.update()
    clock.tick(60)
