import cv2
import numpy as np
import os
def convert_to_grayscale_cv(image_path, output_path):
    color_image = cv2.imread(image_path)
    
    # 根据给定公式转换为灰度图像
    gray_image = 0.3 * color_image[:, :, 2] + 0.59 * color_image[:, :, 1] + 0.11 * color_image[:, :, 0]
    gray_image = gray_image.astype(np.uint8)
    
    # 保存灰度图像
    cv2.imwrite(output_path, gray_image)


def add_two_images_grayscale(image_path1, image_path2,temp_gray_path1,temp_gray_path2, output_path):

    convert_to_grayscale_cv(image_path1, temp_gray_path1)
    convert_to_grayscale_cv(image_path2, temp_gray_path2)

    img1 = cv2.imread(temp_gray_path1)
    img2 = cv2.imread(temp_gray_path2)

    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # plus
    result_img = cv2.add(img1, img2)

    # 保存结果
    cv2.imwrite(output_path, result_img)

    return output_path

# 调用函数
result_path = add_two_images_grayscale(
    'arlisgreat/ColorfulDragon.jpg',
    'arlisgreat/ColorfulMorning.jpg',
    'arlisgreat/GrayDragon.jpg',
    'arlisgreat/GrayMorning.jpg',
    'arlisgreat/plus.jpg'
)

print(f"结果图片已保存到: {result_path}")
