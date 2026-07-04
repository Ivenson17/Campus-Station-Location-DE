import numpy as np
import pandas as pd


class CampusStationObjective:

    # 读取数据
    def __init__(self, data_path):

        self.df = pd.read_csv(data_path)

        self.x_points = self.df["x"].values
        self.y_points = self.df["y"].values
        self.weights = self.df["demand"].values

    # 计算目标函数
    def evaluate(self, position):

        x = position[0]
        y = position[1]

        distances = np.sqrt(
            (x - self.x_points) ** 2 +
            (y - self.y_points) ** 2
        )

        fitness = np.sum(
            self.weights * distances
        )

        # 返回适应度
        return fitness
    
    def __call__(self, position):
        return self.evaluate(position)