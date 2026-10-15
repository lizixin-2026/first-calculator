import tkinter as tk  #做窗口和画布
import random  #随机生成食物位置

# 游戏配置
WIDTH = 400  #画布宽度
HEIGHT = 400  #画布高度
CELL = 20  #每格20像素 食物和蛇按格走
SPEED = 200  #200毫秒刷新一次 数字越小越快

class SnakeGame:  #定义一个名叫snakegame的类
    def __init__(self, root):  #初始化函数
        self.root = root  #窗口存到self.root
        self.root.title("贪吃蛇")  #标题
        self.root.resizable(False, False)  #禁止拉伸

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()  #创建黑色画布 pack()放进窗口

        self.score = 0  #当前得分 初始0
        self.score_label = tk.Label(root, text=f"得分: {self.score}", font=("Arial", 14))
        self.score_label.pack()  #显示得分文字标签 放画布下面

        self.root.bind("<KeyPress>", self.change_direction)
        self.reset_game()  #初始化蛇的位置方向食物
        self.root.after(SPEED, self.game_loop)

    def reset_game(self):
        # 蛇初始位置（3节）
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"
        self.next_direction = "Right"
        self.food = self.random_food()
        self.score = 0
        self.score_label.config(text=f"得分: {self.score}")
        self.game_over = False

    def random_food(self):
        while True:
            x = random.randint(0, (WIDTH // CELL) - 1) * CELL
            y = random.randint(0, (HEIGHT // CELL) - 1) * CELL
            if (x, y) not in self.snake:
                return (x, y)

    def change_direction(self, event):
        key = event.keysym
        if key == "Up" and self.direction != "Down":
            self.next_direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.next_direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.next_direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.next_direction = "Right"

    def move_snake(self):
        self.direction = self.next_direction
        head_x, head_y = self.snake[0]

        if self.direction == "Up":
            head_y -= CELL
        elif self.direction == "Down":
            head_y += CELL
        elif self.direction == "Left":
            head_x -= CELL
        elif self.direction == "Right":
            head_x += CELL

        new_head = (head_x, head_y)

        # 撞墙或撞自己
        if (head_x < 0 or head_x >= WIDTH or
            head_y < 0 or head_y >= HEIGHT or
            new_head in self.snake):
            self.game_over = True
            return

        self.snake.insert(0, new_head)

        # 吃到食物
        if new_head == self.food:
            self.score += 10
            self.score_label.config(text=f"得分: {self.score}")
            self.food = self.random_food()
        else:
            self.snake.pop()

    def draw(self):
        self.canvas.delete("all")

        # 画食物
        fx, fy = self.food
        self.canvas.create_oval(fx, fy, fx + CELL, fy + CELL, fill="red")

        # 画蛇
        for i, (x, y) in enumerate(self.snake):
            color = "green" if i == 0 else "lightgreen"
            self.canvas.create_rectangle(x, y, x + CELL, y + CELL, fill=color)

        if self.game_over:
            self.canvas.create_text(
                WIDTH // 2, HEIGHT // 2,
                text="游戏结束\n按 R 重新开始",
                fill="white", font=("Arial", 20), justify="center"
            )

    def game_loop(self):
        if not self.game_over:
            self.move_snake()
        self.draw()
        self.root.after(SPEED, self.game_loop)

    def restart(self, event):
        if self.game_over and event.keysym.lower() == "r":
            self.reset_game()
            self.root.focus_force()


if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.bind("<KeyPress-r>", game.restart)
    root.mainloop()
