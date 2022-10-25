import cv2  # 导入OpenCV-Python包
# 读取图像 lena.png保存在当前目录下
lena = cv2.imread("lena.png")  
# 显示图像
cv2.imshow('demo1',lena)
# 保存图像
r = cv2.imwrite("another_lena.png", lena) 
print(cv2.__version__)