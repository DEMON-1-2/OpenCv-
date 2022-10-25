import numpy as np
import cv2
# 初始化当前摄像头
cap = cv2.VideoCapture(0)
# 设置视频编码,解码格式：以下是未压缩的YUV颜色编码格式
fourcc = cv2.VideoWriter_fourcc('I','4','2','0')
# 保存视频文件"output.avi"",视频编解码格式,帧速率,视频的长宽度
out = cv2.VideoWriter('output.avi', fourcc, 20, (640,480))
# 检查摄像头是否初始化成功，进入循环
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)
        cv2.imshow('frame', frame)
        # 按下ESC(27)键退出使用摄像头,播放每一帧停留25ms
        if cv2.waitKey(20) & 0xFF == 27:
            break
    else:
        break
cap.release()  # 关闭摄像头
out.release()  # 释放cv2.VideoWriter()对象
cv2.destroyAllWindows()  # 关闭窗口