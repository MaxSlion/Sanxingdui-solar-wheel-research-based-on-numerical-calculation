import cv2
import numpy as np

def contrast_stretching(image):
    # 线性拉伸对比度增强
    min_value = np.min(image)
    max_value = np.max(image)
    enhanced_image = np.clip((image - min_value) * 255.0 / (max_value - min_value), 0, 255).astype(np.uint8)
    return enhanced_image

def main():
    # 读取图像
    image = cv2.imread('./sunwhaeler.jpg', cv2.IMREAD_GRAYSCALE)

    # 对图像进行二值化处理
    threshold_value = 150
    _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

    # 对二值化图像进行对比度增强
    enhanced_image = contrast_stretching(binary_image)

    # 寻找物体轮廓
    contours, _ = cv2.findContours(enhanced_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 绘制轮廓
    contour_image = cv2.cvtColor(enhanced_image, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

    # 显示原始图像和包含轮廓的图像
    cv2.imshow('Original Image', image)
    cv2.imshow('Contour Image', contour_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()
