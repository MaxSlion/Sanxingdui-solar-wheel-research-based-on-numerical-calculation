import cv2
def calculate_black_area(image_path):
    # 读取图像
    image = cv2.imread(image_path)
    # 获取图像的行数和列数
    rows, cols, _ = image.shape
    # 计算黑色像素数量
    black_pixels = 0
    for row in range(rows):
        for col in range(cols):
            # 图像像素是一个三元组 (B, G, R)
            # 当B, G, R都为0时，表示黑色像素
            if all(image[row, col] == [0, 0, 0]):
                black_pixels += 1
    # 计算黑色区域的面积（假设图像的每个像素代表一个单位面积）
    total_pixels = rows * cols
    black_area = black_pixels / total_pixels
    return black_area
# 替换为您的图像文件路径
image_path = './difference_from_origin_and_repair_binary.png'
black_area = calculate_black_area(image_path)
print("黑色区域的面积：", black_area)
