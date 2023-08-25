import matplotlib.pyplot as plt
import numpy as np

def calculate_bezier_curve(points):
    # 二次贝塞尔曲线公式为 P(t) = (1-t)^2 * P0 + 2 * (1-t) * t * P1 + t^2 * P2
    # 其中 P0, P1, P2 分别为起始点、控制点和结束点，t 为取值范围在 [0, 1] 的参数
    t = np.linspace(0, 1, 100)
    x_points = np.array([p[0] for p in points])
    y_points = np.array([p[1] for p in points])

    bezier_x = (1 - t)**2 * x_points[0] + 2 * (1 - t) * t * x_points[1] + t**2 * x_points[2]
    bezier_y = (1 - t)**2 * y_points[0] + 2 * (1 - t) * t * y_points[1] + t**2 * y_points[2]

    return bezier_x, bezier_y

def plot_bezier_curve(bezier_x, bezier_y, points):
    plt.plot(bezier_x, bezier_y, label='Bezier Curve')
    plt.scatter([p[0] for p in points], [p[1] for p in points], color='red', label='Control Points')
    plt.legend()
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Quadratic Bezier Curve')
    plt.grid(True)
    plt.show()

def main():
    # 读取用户输入的坐标点数据，以 (x, y) 形式存储在列表中
    points = []
    for i in range(3):
        x = float(input(f"请输入第{i + 1}个坐标点的X值："))
        y = float(input(f"请输入第{i + 1}个坐标点的Y值："))
        points.append((x, y))

    bezier_x, bezier_y = calculate_bezier_curve(points)
    plot_bezier_curve(bezier_x, bezier_y, points)

if __name__ == "__main__":
    main()
