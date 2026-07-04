import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ==========================
# 读取需求点数据
# ==========================
df = pd.read_csv("data/demand_points.csv")

x = df["x"]
y = df["y"]
demand = df["demand"]

# ==========================
# 图1：需求点分布图
# ==========================
plt.figure(figsize=(8, 5))

# 绘制散点图
plt.scatter(
    x,
    y,
    s=demand,
)

# 给每个点编号
for i in range(len(df)):
    plt.annotate(
        str(i + 1),
        (x[i], y[i])
    )

plt.xlabel("X")
plt.ylabel("Y")

plt.title("Campus Demand Points")

# 设置显示范围
plt.xlim(0, 50)
plt.ylim(0, 30)

plt.grid(True)

plt.savefig(
    "results/demand_points.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# ==========================
# 图2：目标函数地形图
# ==========================

X = np.linspace(0, 50, 100)
Y = np.linspace(0, 30, 100)

X_grid, Y_grid = np.meshgrid(X, Y)

Z = np.zeros_like(X_grid)

for idx in range(len(df)):

    # 读取需求点信息
    xi = df.loc[idx, "x"]
    yi = df.loc[idx, "y"]
    wi = df.loc[idx, "demand"]

    # 计算目标函数
    Z += wi * np.sqrt(
        (X_grid - xi) ** 2 + (Y_grid - yi) ** 2
    )
    # Z为(100×100)Matrix

plt.figure(figsize=(10, 6))

# 绘制等高填色图
contour = plt.contourf(
    X_grid,
    Y_grid,
    Z,
    levels=30
)

plt.colorbar(contour)

plt.scatter(
    x,
    y,
    marker="o"
)

# 编号
for i in range(len(df)):
    plt.annotate(
        str(i + 1),
        (x[i], y[i])
    )

plt.xlabel("X")
plt.ylabel("Y")

plt.title(
    "Objective Function Landscape"
)

plt.savefig(
    "results/objective_landscape.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Demand points figure saved.")
print("Objective landscape figure saved.")