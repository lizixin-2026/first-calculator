import cv2  #Open CV在python中的名字

# 加载 OpenCV 自带的人脸检测模型
face_cascade = cv2.CascadeClassifier(  #创建一个分类器
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)  #模型文件夹 + 训练好的正面人脸检测文件


# cap摄像头对象 = 打开摄像头，0 通常是电脑默认单个摄像头
cap = cv2.VideoCapture(0)


if not cap.isOpened():  #检查摄像头是否打开
    print("无法打开摄像头，请检查权限或是否被其他程序占用")
    exit()  #结束整个程序

print("摄像头已打开，切换英文输入，按 q 退出")

while True:
    # ret布尔值(true/false) frame图像数据 读取一帧画面
    ret, frame = cap.read()
    if not ret:
        print("读取画面失败")
        break

    # 转成灰度图，检测更快 由BGR彩图转灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 检测人脸
    faces = face_cascade.detectMultiScale(  #用之前加载的模型来检测人脸
        gray,
        scaleFactor=1.1,  #每次把图像缩小1.1倍来检测
        minNeighbors=5,
        minSize=(30, 30)  #最小人脸尺寸
    )

    # 给每张脸画绿框
    for (x, y, w, h) in faces:  #faces检测到的人脸列表
        #图像上画矩形框 矩形左上角，右下角，绿色，框粗细（像素）
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #图像上写文字“face” 文字位置
        cv2.putText(frame, "Face", (x, y - 10),
                    #字体样式 大小 颜色 字粗细
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # 左上角显示检测到的人脸数
    cv2.putText(frame, f"Faces: {len(faces)}", (10, 30),  #检测到的人脸数量
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # 显示画面
    cv2.imshow('Face Detection', frame)  #弹出显示图像窗口（窗口标题，图像）

    # 按 q 退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  #循环结束后 释放摄像头资源 防止一直被占用
cv2.destroyAllWindows()  #关闭所有opencv窗口

