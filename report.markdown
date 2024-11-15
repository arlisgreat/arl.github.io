# CV_L02 数字图像基础编程作业

>**Task1** 对一幅灰度图像进行线性点运算，输出相应的图像。
>**Task2** 将两幅彩色图像分别转换为灰度图像;进一步地，对得到的两幅灰度图像进行加运算，输出相应的图像。

---
## Task1


对灰度图像进行线性点运算可以用以下公式表示：
\[
g(x, y) = a \cdot f(x, y) + b
\]
其中，\( g(x, y) \) 是变换后的图像的像素值，\( f(x, y) \) 是原始图像的像素值，系数 \( a = 1.5 \) 和偏置 \( b = 20 \)。

```def linear_point_operation_cv(image_path,output_path,a, b):
    img = cv2.imread(image_path) 
    # linearDotOperation
    transformed_img = cv2.addWeighted(img, a, np.zeros_like(img), 0, b)
    # demonstrate
    cv2.imwrite(output_path, transformed_img)
    cv2.imshow('After Operation', transformed_img)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()
```

<div style="text-align: center;">
  <div style="display: inline-block; margin-right: 10px;">
    <img src="GrayDragon.jpg" alt="Before" width="300px">
    <figcaption style="text-align: center;">Before</figcaption>
  </div>
  <div style="display: inline-block;">
    <img src="linear.jpg" alt="After" width="300px">
    <figcaption style="text-align: center;">After</figcaption>
  </div>
</div>

---
## Task2



将彩色图像转换为灰度图像的标准公式为：
\[
g(x, y) = 0.3 \cdot R(x, y) + 0.59 \cdot G(x, y) + 0.11 \cdot B(x, y)
\]

其中，\(g(x, y)\) 是灰度图像在位置 \((x, y)\) 的像素值，而 \(R(x, y)\)，\(G(x, y)\)，和 \(B(x, y)\) 分别是原彩色图像在同一位置的红色、绿色和蓝色通道的像素值。
```def convert_to_grayscale_cv(image_path, output_path):
    color_image = cv2.imread(image_path)
    # formula
    gray_image = 0.3 * color_image[:, :, 2] + 0.59 * color_image[:, :, 1] + 0.11 * color_image[:, :, 0]
    gray_image = gray_image.astype(np.uint8)
    # save
    cv2.imwrite(output_path, gray_image)
    # demonstrate
    cv2.imshow('GrayScale Image', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```

<div style="text-align: center;">
  <div style="display: inline-block; margin-right: 10px;">
    <img src="ColorfulDragon.jpg" alt="Before" width="200px">
    <figcaption style="text-align: center;">Before</figcaption>
  </div>
  <div style="display: inline-block;">
    <img src="GrayDragon.jpg" alt="After" width="200px">
    <figcaption style="text-align: center;">After</figcaption>
  </div>
</div>

<div style="text-align: center;">
  <div style="display: inline-block; margin-right: 10px;">
    <img src="ColorfulMorning.jpg" alt="Before" width="300px">
    <figcaption style="text-align: center;">Before</figcaption>
  </div>
  <div style="display: inline-block;">
    <img src="GrayMorning.jpg" alt="After" width="300px">
    <figcaption style="text-align: center;">After</figcaption>
  </div>
</div>
<br>
<br>

进行图像像素加运算之前，保证图像大小相同，采用 <code>cv2.resize()</code>
<code>img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))</code>

<div style="text-align: center;">
  <div style="display: inline-block; margin-right: 10px;">
    <img src="plus.jpg" alt="Before" width="300px">
    <figcaption style="text-align: center;">plus</figcaption>
  </div>
  
</div>
