import matplotlib.pyplot as plt
import numpy as np
mid = [(0,0)]
coordinates = []
intersection_points = []
inradius = 5
focus = -0x3f3f3f3f
def divide_circle(divisions):
    angle_offset = np.radians(((360 / divisions) / 2))
    angle_increment = (360 / divisions)
    for i in range(divisions):
        angle = np.radians(i * angle_increment) + angle_offset
        x = 5 * np.cos(angle)
        y = 5 * np.sin(angle)
        coordinates.append((x, y))
    return coordinates
def rotate_hyperbola(a, b, angle):
    theta = np.radians(angle)
    x_hyperbola = np.linspace(-a * 5, a * 5, 1000)
    y_hyperbola = np.sqrt((x_hyperbola ** 2 / a ** 2 - 1) * b ** 2)
    # 旋转双曲线
    x_rotated = x_hyperbola * np.cos(theta) - y_hyperbola * np.sin(theta)
    y_rotated = x_hyperbola * np.sin(theta) + y_hyperbola * np.cos(theta)
    plt.plot(x_rotated, y_rotated, color='purple', linestyle='--')
    plt.plot(x_rotated, -y_rotated, color='purple', linestyle='--')
def find_intersection(p1, p2, p3, p4):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denominator == 0:
        return None
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denominator
    u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denominator
    if 0 <= t <= 1 and 0 <= u <= 1:
        x_intersect = round(x1 + t * (x2 - x1), 5)
        y_intersect = round(y1 + t * (y2 - y1), 5)
        return x_intersect, y_intersect
    else:
        return None
def draw_circle(num):
    global inradius, focus, inradius_x, inradius_y
    coordinate = divide_circle(num)
    fig, ax = plt.subplots()
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    # 绘制虚线坐标轴
    ax.axhline(0, linestyle='dashed', color='gray')
    ax.axvline(0, linestyle='dashed', color='gray')
    ax.set_xticks(range(-5, 6))
    ax.set_yticks(range(-5, 6))
    ax.grid()
    circle = plt.Circle((0, 0), 5, edgecolor='black', facecolor='None')
    ax.add_patch(circle)
    for i in range(len(coordinates) - 1):
        for j in range(i + 1, len(coordinates)):
            p1, p2 = coordinates[i], coordinates[j]
            for k in range(i + 1, len(coordinates)):
                for l in range(k + 1, len(coordinates)):
                    p3, p4 = coordinates[k], coordinates[l]
                    intersection = find_intersection(p1, p2, p3, p4)
                    if intersection:
                        intersection_points.append(intersection)
    # 使用set进行去重
    intersection_set = set()
    for i in range(len(coordinates) - 1):
        for j in range(i + 1, len(coordinates)):
            p1, p2 = coordinates[i], coordinates[j]
            for k in range(i + 1, len(coordinates)):
                for l in range(k + 1, len(coordinates)):
                    p3, p4 = coordinates[k], coordinates[l]
                    intersection = find_intersection(p1, p2, p3, p4)
                    if intersection:
                        intersection_set.add(intersection)
    # 对coordinates中的数据保留五位小数
    coordinates_dis = [(round(x, 5), round(y, 5)) for x, y in coordinates]
    # 去除coordinates中已有的元素
    intersection_points_dis = list(intersection_set.difference(coordinates_dis,mid))
    # 全连接等分点
    for i, (x1, y1) in enumerate(coordinate, 1):
        for x2, y2 in coordinate[i:]:
            ax.plot([x1, x2], [y1, y2], linestyle='--', color='blue')
    # # 标记等分点位置并打印等分点坐标
    for label, (x, y) in enumerate(coordinates_dis, 1):
        # ax.text(x, y, f"P{str(label)}")
        print(f"顶点P{str(label)}: {(round(x, 1), round(y, 1))}")
        if label == 1:
            inradius_x = np.abs(round(x, 1))
            inradius_y = np.abs(round(y, 1))
            print("内接圆半径：", inradius_y)
    # # 标记交点位置并打印交点坐标
    for i, (x, y) in enumerate(intersection_points_dis, 1):
        # ax.plot(x, y, marker='o', markersize=4, color='red')
        # ax.text(x + 0.2, y + 0.2, f"F{str(i)}", color = 'red')
        print(f'交点F{i}:{(round(x, 1),round(y ,1))}')
    if num_divisions != 4:
        circle1 = plt.Circle((0, 0), inradius_y, linestyle='dashed', edgecolor='black', facecolor='None')
        ax.add_patch(circle1)
    circle2 = plt.Circle((0, 0), 4.2, linestyle='dashed', edgecolor='black', facecolor='None')
    ax.add_patch(circle2)
    ax.text(mid[0][0] + 0.2, mid[0][1] + 0.2, f"F")
    print("圆心：",mid)
    # 添加双曲线
    angle_offset = 360 / num_divisions
    angles = np.arange(0, 360, angle_offset)
    if num_divisions != 4:
        a = inradius_y
        k = round((inradius_y / inradius_x), 1)
        b = k * a
    else:
        a = 1.55
        b = 1.12
    print("inradius:", a, "k:", k, "b:", b)
    for angle in angles:
        theta = np.radians(angle)
        x_hyperbola = np.linspace(-a * 3, a * 3, 1000)
        y_hyperbola = np.sqrt((x_hyperbola ** 2 / a ** 2 - 1) * b ** 2)
        x_rotated = x_hyperbola * np.cos(theta) - y_hyperbola * np.sin(theta)
        y_rotated = x_hyperbola * np.sin(theta) + y_hyperbola * np.cos(theta)
        plt.plot(x_rotated, y_rotated, color='purple', linestyle='--')
        plt.plot(x_rotated, -y_rotated, color='purple', linestyle='--')
    plt.show()
# 输入需要等分的数量
num_divisions = int(input("输入需要等分的数量: "))
# 绘图
draw_circle(num_divisions)
