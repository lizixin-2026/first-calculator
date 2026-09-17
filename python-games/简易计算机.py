def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "错误：不能除以 0"
    return a / b

def calculator():
    print("=== 简易计算器 ===")
    print("a. 加法")
    print("b. 减法")
    print("c. 乘法")
    print("d. 除法")
    print("e. 退出")

    while True:
        choice = input("\\n请选择操作（a-e）：")

        if choice == "e":
            print("关闭计算机")
            break

        if choice not in ["a", "b", "c", "d"]:
            print("输入无效，请输入 a-d或e")
            continue

        try:
            num1 = float(input("请输入第一个数字："))
            num2 = float(input("请输入第二个数字："))
        except ValueError:
            print("错误：请输入数字")
            continue

        if choice == "a":
            result = add(num1, num2)
            fh = "+"
        elif choice == "b":
            result = subtract(num1, num2)
            fh = "-"
        elif choice == "c":
            result = multiply(num1, num2)
            fh = "*"
        elif choice == "d":
            result = divide(num1, num2)
            fh = "/"

        print(f"结果：{num1} {fh} {num2} = {result}")

if __name__ == "__main__":
    calculator()
