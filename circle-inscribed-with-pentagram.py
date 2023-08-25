import numpy as np
import matplotlib.pyplot as plt
def draw_star(center, radius):
    # 计算五角星的五个顶点坐标
    angles = np.linspace(0, 2 * np.pi, 6)[:-1]
    star_points = [(center[0] + radius * np.cos(angle), center[1] + radius * np.sin(angle)) for angle in angles]
    # 绘制圆
    circle = plt.Circle(center, radius, fill=False, color='blue')
    plt.gca().add_patch(circle)
    # 绘制五角星
    star = plt.Polygon(star_points, fill=False, color='red')
    plt.gca().add_patch(star)
    # 绘制五角星的五个顶点到圆心的连线
    focus_points = []
    # 存储焦点坐标和外圆的顶点
    points_dict = {'C': center}
    for i in range(5):
        point_label = chr(65 + i)  # 使用字母标记点，A对应索引0，B对应索引1，以此类推
        points_dict[point_label] = star_points[i]
        plt.plot([center[0], star_points[i][0]], [center[1], star_points[i][1]], color='green')
        # 绘制相隔一个点的连线
        next_index = (i + 2) % 5
        plt.plot([star_points[i][0], star_points[next_index][0]], [star_points[i][1], star_points[next_index][1]], color='green')
        # 计算焦点坐标并添加到列表中
        focus_x = (star_points[i][0] + star_points[next_index][0]) / 2
        focus_y = (star_points[i][1] + star_points[next_index][1]) / 2
        focus_points.append((focus_x, focus_y))
    # 设置画布大小和坐标轴范围
    plt.axis('equal')
    plt.xlim(center[0] - radius, center[0] + radius)
    plt.ylim(center[1] - radius, center[1] + radius)
    # 绘制内切圆
    for i, focus_point in enumerate(focus_points):
        distance = np.sqrt(focus_point[0]**2 + focus_point[1]**2)  # 计算焦点与圆心的距离
        tangent_circle = plt.Circle(center, distance, fill=False, color='orange', linestyle='dashed')
        plt.gca().add_patch(tangent_circle)
    print("distance is:",distance)
    # 标注焦点坐标
    for i, focus_point in enumerate(focus_points):
        plt.text(focus_point[0], focus_point[1], f'F{i+1}', color='black', fontsize=12)
    print(focus_points)
    # 标注点的字母标记
    for label, point in points_dict.items():
        plt.text(point[0], point[1], label, ha='center', va='center', fontsize=12)
    print(points_dict)
    # 显示图像
    plt.show()
def main():
    center = (0, 0)  # 圆心坐标
    radius = 5      # 圆的半径
    draw_star(center, radius)
if __name__ == '__main__':
    main()
