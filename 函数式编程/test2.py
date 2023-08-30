import numpy as np
import matplotlib.pyplot as plt

# 定义正态分布的均值和标准差
mu = 0  # 均值
sigma = 1  # 标准差

# 生成一组 x 值，从 -4 到 4，间隔为 0.1
x = np.arange(-4, 4, 0.1)

# 计算对应于 x 值的正态分布的累积分布函数值
y = 0.5 * (1 + np.erf((x - mu) / (sigma * np.sqrt(2))))

# 绘制正态分布的累积分布函数图像
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('Cumulative Distribution Function')
plt.title('Normal Distribution CDF')
plt.grid(True)
plt.show()
