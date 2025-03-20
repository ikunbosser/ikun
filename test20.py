import numpy as np
import matplotlib.pyplot as plt

# 定义函数 f(x)
def f(x):
    return x**2 * np.sin(1/x)

# 定义导函数 f'(x)
def f_prime(x):
    return 2*x * np.sin(1/x) - np.cos(1/x)

# 生成 x 值，避开 x=0 附近的奇点
x = np.linspace(-0.5, 0.5, 5000)
x = x[np.abs(x) > 1e-5]  # 去掉 x=0 附近的点，避免除零错误

# 计算函数值和导数值
y = f(x)
y_prime = f_prime(x)

# 绘制函数 f(x)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x, y, label=r'$f(x) = x^2 \sin(1/x)$', color='blue')
plt.title('Function $f(x)$')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.grid(True)
plt.legend()

# 绘制导函数 f'(x)
plt.subplot(1, 2, 2)
plt.plot(x, y_prime, label=r"$f'(x) = 2x \sin(1/x) - \cos(1/x)$", color='red')
plt.title("Derivative $f'(x)$")
plt.xlabel('$x$')
plt.ylabel("$f'(x)$")
plt.grid(True)
plt.legend()

# 显示图像
plt.tight_layout()
plt.show()