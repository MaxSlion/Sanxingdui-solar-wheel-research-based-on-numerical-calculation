import matplotlib.pyplot as plt
import numpy as np
def find_intersection_point(p1, p2, p3, p4):
    # 寻找线段p1p2和线段p3p4的交点
    x_num = (p1[0] * p2[1] - p1[1] * p2[0]) * (p3[0] - p4[0]) - (p1[0] - p2[0]) * (p3[0] * p4[1] - p3[1] * p4[0])
    x_denom = (p1[0] - p2[0]) * (p3[1] - p4[1]) - (p1[1] - p2[1]) * (p3[0] - p4[0])

    y_num = (p1[0] * p2[1] - p1[1] * p2[0]) * (p3[1] - p4[1]) - (p1[1] - p2[1]) * (p3[0] * p4[1] - p3[1] * p4[0])
    y_denom = (p1[0] - p2[0]) * (p3[1] - p4[1]) - (p1[1] - p2[1]) * (p3[0] - p4[0])
    if x_denom == 0 or y_denom == 0:
        raise ValueError("Lines are parallel and do not intersect.")
    intersection_x = x_num / x_denom
    intersection_y = y_num / y_denom
    return intersection_x, intersection_y
star_points = []
focus_points = []
distance = 0
radius1 = 4.2
intersections = []
edges = [('B', 'D'), ('B', 'E'), ('C', 'A'), ('C', 'E'), ('A', 'D')]
intersection_points = []
def draw_star(center, radius):
    angle_offset = np.radians(54)
    # 计算五角星的五个顶点坐标，并让一个顶点朝上
    angles = (np.linspace(0, 2 * np.pi, 6)[:-1] + np.pi / 10 ) + angle_offset
    star_points = [(center[0] + radius * np.cos(angle), center[1] + radius * np.sin(angle)) for angle in angles]
    # 绘制圆
    circle = plt.Circle(center, radius, fill=False, color='blue')
    circle1 = plt.Circle(center, radius1, fill=False, color='blue')
    plt.gca().add_patch(circle)
    plt.gca().add_patch(circle1)
    # 绘制五角星
    star = plt.Polygon(star_points, fill=False, color='red')
    # 绘制五角星的五个顶点到圆心的连线
    plt.gca().add_patch(star)
    focus_pointss = []
    # 存储焦点坐标和外圆的顶点
    points_dict = {'C': center, 'F': (0, 0)}
    for i in range(5):
        point_label = chr(65 + i)  # 使用字母标记点，A对应索引0，B对应索引1，以此类推
        points_dict[point_label] = star_points[i]
        plt.plot([center[0], star_points[i][0]], [center[1], star_points[i][1]], color='green')
        # 绘制相隔一个点的连线
        next_index = (i + 2) % 5
        plt.plot([star_points[i][0], star_points[next_index][0]], [star_points[i][1], star_points[next_index][1]],color='green')
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
        # 计算焦点与圆心的距离
        distance = np.sqrt(focus_point[0] ** 2 + focus_point[1] ** 2)
        # 绘制内切圆
        tangent_circle = plt.Circle(center, distance, fill=False, color='orange', linestyle='dashed')
        plt.gca().add_patch(tangent_circle)
        # 计算新的焦点坐标（顺时针旋转36°）
        new_x = focus_point[0] * np.cos(np.radians(36)) - focus_point[1] * np.sin(np.radians(36))
        new_y = focus_point[0] * np.sin(np.radians(36)) + focus_point[1] * np.cos(np.radians(36))
        # 绘制新坐标的标记点
        plt.scatter(new_x, new_y, color='orange')
        # 将新焦点坐标追加到focus_points列表中
        focus_pointss.append((new_x, new_y))
    print("distance is:", distance)
    # 标注焦点坐标
    focus_points.extend(focus_pointss)
    for i, focus_point in enumerate(focus_points):
        plt.text(focus_point[0], focus_point[1], f'F{i + 1}', color='black', fontsize=12)
    print(focus_points)
    # 标注点的字母标记
    for label, point in points_dict.items():
        plt.text(point[0], point[1], label, ha='center', va='center', fontsize=12)
    print(points_dict)
    # 计算内切圆与线段的交点
    def circle_line_intersection(circle_radius, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        dx = x2 - x1
        dy = y2 - y1
        dr = np.sqrt(dx ** 2 + dy ** 2)
        D = x1 * y2 - x2 * y1
        discriminant = circle_radius ** 2 * dr ** 2 - D ** 2
        if discriminant >= 0:
            x_intersection1 = (D * dy + np.sign(dy) * dx * np.sqrt(discriminant)) / dr ** 2
            y_intersection1 = (-D * dx + np.abs(dy) * np.sqrt(discriminant)) / dr ** 2
            x_intersection2 = (D * dy - np.sign(dy) * dx * np.sqrt(discriminant)) / dr ** 2
            y_intersection2 = (-D * dx - np.abs(dy) * np.sqrt(discriminant)) / dr ** 2
            return [(x_intersection1, y_intersection1), (x_intersection2, y_intersection2)]
        else:
            return []
    # 计算circle1（内切圆）与线段BD、BE、CA、CE、AD的交点，并存在列表中
    line_segments = [(points_dict['B'], points_dict['D']), (points_dict['B'], points_dict['E']),
                     (points_dict['C'], points_dict['A']), (points_dict['C'], points_dict['E']),
                     (points_dict['A'], points_dict['D'])]
    for segment in line_segments:
        points = circle_line_intersection(radius1, segment[0], segment[1])
        intersections.extend(points)
    # 线段BE与线段AC的交点
    intersection_point_BE_AC = find_intersection_point(points_dict['B'], points_dict['E'], points_dict['A'],points_dict['C'])
    plt.scatter(*intersection_point_BE_AC, color='purple', marker='x')
    intersection_points.append(intersection_point_BE_AC)
    # 线段BE与线段AD的交点
    intersection_point_BE_AD = find_intersection_point(points_dict['B'], points_dict['E'], points_dict['A'],points_dict['D'])
    plt.scatter(*intersection_point_BE_AD, color='purple', marker='x')
    intersection_points.append(intersection_point_BE_AD)
    # 线段CE与线段DB的交点
    intersection_point_CE_DB = find_intersection_point(points_dict['C'], points_dict['E'], points_dict['D'],points_dict['B'])
    plt.scatter(*intersection_point_CE_DB, color='purple', marker='x')
    intersection_points.append(intersection_point_CE_DB)
    # 线段CE与线段DA的交点
    intersection_point_CE_DA = find_intersection_point(points_dict['C'], points_dict['E'], points_dict['D'],points_dict['A'])
    plt.scatter(*intersection_point_CE_DA, color='purple', marker='x')
    intersection_points.append(intersection_point_CE_DA)
    # 线段DB与线段AC的交点
    intersection_point_DB_AC = find_intersection_point(points_dict['D'], points_dict['B'], points_dict['A'],points_dict['C'])
    plt.scatter(*intersection_point_DB_AC, color='purple', marker='x')
    intersection_points.append(intersection_point_DB_AC)
    # 标注交点坐标
    for i, intersection_point in enumerate(intersection_points):
        plt.text(intersection_point[0], intersection_point[1], f'P{i + 1}', color='purple', fontsize=12)
        print(f"P{i+1}:({intersection_point[0],intersection_point[1]})")
    # 计算EF的延长线的终点坐标
    F_x, F_y = points_dict["F"]
    EF_extension_x = 3 * focus_points[5][0] - F_x
    EF_extension_y = 3 * focus_points[5][1] - F_y
    # 绘制EF延长线
    plt.plot([F_y, EF_extension_x], [F_x, EF_extension_y], color='purple', linestyle='dashed')
    rotation_angle = np.radians(-90)
    rotated_EF_extension_x = EF_extension_x * np.cos(rotation_angle) - EF_extension_y * np.sin(rotation_angle)
    rotated_EF_extension_y = EF_extension_x * np.sin(rotation_angle) + EF_extension_y * np.cos(rotation_angle)
    plt.plot([-rotated_EF_extension_x, rotated_EF_extension_x], [-rotated_EF_extension_y, rotated_EF_extension_y],color='black', linestyle='dashed')
    # 输入点的坐标
    B = points_dict["B"]
    new_Bx = B[0]
    new_By = B[1]
    # 添加双曲线
    a = 1.55
    k = round(new_By / new_Bx, 1)
    b = round(a * k, 2)
    x_hyperbola = np.linspace(-a * 5, a * 5, 1000)
    y_hyperbola = np.sqrt((x_hyperbola ** 2 / a ** 2 - 1) * b ** 2)
    plt.plot(x_hyperbola, y_hyperbola, color='purple', linestyle='--', label='Hyperbola: x^2/1.55^2 - y^2/0.93^2 = 1')
    plt.plot(x_hyperbola, -y_hyperbola, color='purple', linestyle='--')
    plt.show()
def main():
    center = (0, 0)  # 圆心坐标
    radius = 5  # 圆的半径
    draw_star(center, radius)
if __name__ == '__main__':
    main()
