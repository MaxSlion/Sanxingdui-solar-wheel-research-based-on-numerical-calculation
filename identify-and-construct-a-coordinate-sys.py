import cv2
import numpy as np
def contrast_stretching(image):
    # 线性拉伸对比度增强
    min_value = np.min(image)
    max_value = np.max(image)
    enhanced_image = np.clip((image - min_value) * 255.0 / (max_value - min_value), 0, 255).astype(np.uint8)
    return enhanced_image
def update_threshold(threshold_value):
    _, binary_image = cv2.threshold(image_gray, threshold_value, 255, cv2.THRESH_BINARY)
    enhanced_image = contrast_stretching(binary_image)
    contour_image = cv2.cvtColor(enhanced_image, cv2.COLOR_GRAY2BGR)
    contours, _ = cv2.findContours(enhanced_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)
    cv2.imshow('Contour Image', contour_image)
def main():
    global image_gray
    # 读取图像
    image = cv2.imread('./sunwhaeler.jpg')
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 创建窗口并显示原始图像
    cv2.imshow('Original Image', image)
    # 创建滑块，并设置初始值为150（阈值初始值）
    cv2.createTrackbar('Threshold', 'Original Image', 150, 255, update_threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()
