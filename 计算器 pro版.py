import math  # 开方要用到 math.sqrt()

def add(a, b):
    """加法"""
    return a + b

def subtract(a, b):
    """减法"""
    return a - b

def multiply(a, b):
    """乘法"""
    return a * b

def divide(a, b):
    """除法，防止除以 0"""
    if b == 0:
        return "错误：不能除以 0"
    return a / b

def power(a, b):
    """次方，a 的 b 次方"""
    return a ** b

def sqrt(a):
    """开方，防止负数"""
    if a < 0:
        return "错误：负数不能开平方"
    return math.sqrt(a)

def calculator():
    print("=== 简易计算器 ===")
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 除法")
    print("5. 次方")
    print("6. 开方")
    print("7. 退出")

    while True:
        choice = input("\\n请选择操作（1-7）：").strip()

        if choice == "7":
            print("再见！")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("输入无效，请输入 1-7")
            continue

        # 开方只需要一个数字
        if choice == "6":
            try:
                num = float(input("请输入要开方的数字："))
            except ValueError:
                print("错误：请输入数字")
                continue
            result = sqrt(num)
            print(f"结果：√{num} = {result}")
            continue

        # 其他运算需要两个数字
        try:
            num1 = float(input("请输入第一个数字："))
            num2 = float(input("请输入第二个数字："))
        except ValueError:
            print("错误：请输入数字")
            continue

        if choice == "1":
            result = add(num1, num2)
            op = "+"
        elif choice == "2":
            result = subtract(num1, num2)
            op = "-"
        elif choice == "3":
            result = multiply(num1, num2)
            op = "*"
        elif choice == "4":
            result = divide(num1, num2)
            op = "/"
        elif choice == "5":
            result = power(num1, num2)
            op = "**"

        print(f"结果：{num1} {op} {num2} = {result}")

if __name__ == "__main__":
    calculator()
