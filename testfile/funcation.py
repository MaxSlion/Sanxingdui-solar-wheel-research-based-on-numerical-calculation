import matplotlib.pyplot as plt
import numpy as np

center = (0, 0)  # 圆心坐标
radius = 5
# 绘制二维坐标系
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# 绘制点 F6
F6_x = -1.55
F6_y = 0
plt.scatter(F6_x, F6_y, color='red', label='F6')

# 绘制线段 BF 和 CF
x = np.linspace(-5, 5, 100)
BF_y = -0.725 * x
CF_y = 0.725 * x

plt.plot(x, BF_y, color='blue', label='BF: y = -0.725x')
plt.plot(x, CF_y, color='green', label='CF: y = 0.725x')

# 添加双曲线
a = 1.55
b = 0.96
x_hyperbola = np.linspace(-a * 5, a * 5, 1000)
y_hyperbola = np.sqrt((x_hyperbola ** 2 / a ** 2 - 1) * b ** 2)
plt.plot(x_hyperbola, y_hyperbola, color='purple', linestyle='--', label='Hyperbola: x^2/1.55^2 - y^2/0.93^2 = 1')


# 添加图例
plt.legend()

# 设置坐标轴范围
plt.xlim(center[0] - radius, center[0] + radius)
plt.ylim(center[1] - radius, center[1] + radius)

# 显示网格
plt.grid(True, linestyle='--', alpha=0.7)

# 添加坐标轴标签
plt.xlabel('X')
plt.ylabel('Y')

# 添加标题
plt.title('2D Coordinate System with F6, Line Segments BF and CF, and Hyperbola')

# 显示图像
plt.show()
