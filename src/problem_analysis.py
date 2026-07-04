import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv("data/demand_points.csv")

x = df["x"]
y = df["y"]
demand = df["demand"]

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

plt.show()