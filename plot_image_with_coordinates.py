import cv2
import matplotlib.pyplot as plt
import mplcursors
import numpy as np
def calculate_bezier_curve(points):
    # 二次贝塞尔曲线公式为 P(t) = (1-t)^2 * P0 + 2 * (1-t) * t * P1 + t^2 * P2
    # 当 P1 是极值点时，P1 就是控制点，我们只需计算 P0 和 P2 的坐标
    P0, P1, P2 = points
    t = np.linspace(0, 1, 100)
    bezier_x = (1 - t)**2 * P0[0] + 2 * (1 - t) * t * P1[0] + t**2 * P2[0]
    bezier_y = (1 - t)**2 * P0[1] + 2 * (1 - t) * t * P1[1] + t**2 * P2[1]
    # 打印二次贝塞尔曲线公式
    print("二次贝塞尔曲线公式：")
    print(f"X(t) = (1-t)^2 * {P0[0]} + 2 * (1-t) * t * {P1[0]} + t^2 * {P2[0]}")
    print(f"Y(t) = (1-t)^2 * {P0[1]} + 2 * (1-t) * t * {P1[1]} + t^2 * {P2[1]}\n")
    return bezier_x, bezier_y
def plot_bezier_curve(bezier_x, bezier_y, points):
    plt.plot(bezier_x, bezier_y, label='Bezier Curve')
    plt.scatter([p[0] for p in points], [p[1] for p in points], color='red', label='Control Points')
    plt.legend()
def plot_image_with_coordinates(image_path, x_pixel, y_pixel):
    # 1. 从指定路径读取图片
    image = cv2.imread(image_path)
    # 2. 获取图片的长宽
    height, width, _ = image.shape
    real_x_pixel = width - x_pixel
    print(height, width)
    # 3. 绘制二维坐标系，并将图片作为背景
    fig, ax = plt.subplots()
    ax.imshow(image, extent=[0, width, 0, height])
    # 4. 添加二维坐标系
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    # ax.set_xlabel('X-axis')
    # ax.set_ylabel('Y-axis')
    ax.set_title('Image with 2D Coordinates')
    # 5. 绘制用户输入的像素位置的坐标点
    ax.scatter(x_pixel, y_pixel, color='blue', marker='x', s=50, label='Pixel Position')
    ax.legend()
    # 6. 绘制XY轴线
    ax.axhline(y=y_pixel, color='red', linestyle='-', linewidth=1)
    ax.axvline(x=x_pixel, color='red', linestyle='-', linewidth=1)
    ax.text(x_pixel, height - 10, f"X-axis", color='blue', fontsize=15, ha='center', va='top')
    ax.text(10, y_pixel, f"Y-axis", color='blue', fontsize=15, ha='left', va='center')
    P1_X = 776
    P1_Y = 639
    ax.scatter(P1_X, P1_Y, color='blue', marker='x', s=20)
    ax.text(P1_X + 5, P1_Y + 20, f"(P1:{-(x_pixel - P1_X)}, {P1_Y - y_pixel})", color='red', fontsize=10, ha='center', va='bottom')
    P2_X = 513
    P2_Y = 462
    ax.scatter(P2_X, P2_Y, color='blue', marker='x', s=20)
    ax.text(P2_X + 5, P2_Y + 20, f"(P2:{-(x_pixel - P2_X)}, {P2_Y - y_pixel})", color='red', fontsize=10, ha='center', va='bottom')
    P3_X = 346
    P3_Y = 617
    ax.scatter(P3_X, P3_Y, color='blue', marker='x', s=20)
    ax.text(P3_X + 5, P3_Y + 20, f"(P3:{-(x_pixel - P3_X)}, {P3_Y - y_pixel})", color='red', fontsize=10, ha='center', va='bottom')
    fix_point_x = 533
    fix_point_y = 302
    ax.scatter(fix_point_x, fix_point_y, color='blue', marker='x', s=20)
    ax.text(fix_point_x + 5, fix_point_y + 20, f"(fix_point:{-(x_pixel - fix_point_x)}, {y_pixel - fix_point_y})", color='red', fontsize=10, ha='center', va='bottom')
    P4_X = 24
    P4_Y = 616
    ax.scatter(P4_X, P4_Y, color='blue', marker='x', s=20)
    ax.text(P4_X + 5, P4_Y + 20, f"(P4:{-(x_pixel - P4_X)}, {P4_Y - y_pixel})", color='red', fontsize=10, ha='center', va='bottom')
    P5_X = 116
    P5_Y = 407
    ax.scatter(P5_X, P5_Y, color='blue', marker='x', s=20)
    ax.text(P5_X + 5, P5_Y + 20, f"(P4:{-(x_pixel - P5_X)}, {P5_Y - y_pixel})", color='red', fontsize=10, ha='center', va='bottom')
    P6_X = 179
    P6_Y = 179
    ax.scatter(P6_X, P6_Y, color='blue', marker='x', s=20)
    ax.text(P6_X + 5, P6_Y + 20, f"(P6:{-(x_pixel - P6_X)}, {P6_Y - y_pixel})", color='red', fontsize=10, ha='center', va='bottom')
    points1 = [(776, 639),(533, 302),(346, 617)]
    points2 = [(24, 616),(132, 378),(179, 179)]
    bezier_x, bezier_y = calculate_bezier_curve(points1)
    plot_bezier_curve(bezier_x, bezier_y, points1)
    bezier_x, bezier_y = calculate_bezier_curve(points2)
    plot_bezier_curve(bezier_x, bezier_y, points2)
    # 8. 添加拖动功能
    mplcursors.cursor(hover=True)
# 从用户获取图片路径和像素位置输入
image_path = input("请输入图片路径: ")
x_pixel = int(input("请输入X像素位置: "))
y_pixel = int(input("请输入Y像素位置: "))
def main():
    image_path = "./mask-half.png"
    x_pixel = 832
    y_pixel = 316
    # 调用函数绘制图像和坐标系
    plot_image_with_coordinates(image_path, x_pixel, y_pixel)
    plt.show()
if __name__ == "__main__":
    main()