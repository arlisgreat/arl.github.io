#convert the colored photo to greyscale
#colorful: arlisgreat/ColorfulDragon.jpg
#grey:arlisgreat/GrayDragon.jpg
import cv2
import numpy as np


def convert_to_grayscale_cv(image_path, output_path):
    color_image = cv2.imread(image_path)
    
    # 根据给定公式转换为灰度图像
    gray_image = 0.3 * color_image[:, :, 2] + 0.59 * color_image[:, :, 1] + 0.11 * color_image[:, :, 0]
    gray_image = gray_image.astype(np.uint8)
    
    # 保存灰度图像
    cv2.imwrite(output_path, gray_image)
    
    # 使用OpenCV显示图像
    cv2.imshow('GrayScale Image', gray_image)
    cv2.waitKey(0)  # 等待按键后关闭窗口
    cv2.destroyAllWindows()

# 调用函数，指定输入图像和输出图像的路径
convert_to_grayscale_cv('arlisgreat/ColorfulDragon.jpg', 'arlisgreat/GrayDragon.jpg')

