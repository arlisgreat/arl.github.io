#linear dot opertation on a gray photo
#before operation:
#after operation:
import cv2
import numpy as np

def linear_point_operation_cv(image_path,output_path,a, b):
    img = cv2.imread(image_path) 
    # linearDotOperation
    transformed_img = cv2.addWeighted(img, a, np.zeros_like(img), 0, b)
    # demonstrate
    cv2.imwrite(output_path, transformed_img)
    cv2.imshow('After Operation', transformed_img)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()

# 1.5f+20
linear_point_operation_cv('arlisgreat/GrayDragon.jpg','arlisgreat/linear.jpg',1.5, 20)
