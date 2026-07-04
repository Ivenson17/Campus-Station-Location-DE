import pandas as pd

from src.experiment_runner import run_experiment
from src.de_rand_1_bin import DERand1Bin
from src.de_current_to_best_1_bin import DECurrentToBest1Bin

from src.visualization import (
    plot_convergence,
    plot_boxplot,
    plot_solution
)

from src.objective import CampusStationObjective


# 运行实验
rand_summary, rand_results, rand_histories = run_experiment(
    DERand1Bin, "rand"
)

ctbest_summary, ctbest_results, ctbest_histories = run_experiment(
    DECurrentToBest1Bin, "ctbest"
)


# =========================
# 图1：收敛曲线
# =========================
plot_convergence(rand_histories, ctbest_histories)


# =========================
# 图2：boxplot
# =========================
plot_boxplot(rand_results, ctbest_results)


# =========================
# 图3：最优位置
# =========================
obj = CampusStationObjective("data/demand_points.csv")

best_model = DECurrentToBest1Bin(
    objective=obj,
    bounds=[(0, 50), (0, 30)],
    pop_size=20
)

best, fitness, _ = best_model.optimize(
    generations=50,
    F=0.5,
    CR=0.9
)

import pandas as pd
df = pd.read_csv("data/demand_points.csv")

plot_solution(best, df)