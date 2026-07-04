from src.objective import CampusStationObjective
from src.de_rand_1_bin import DERand1Bin
from src.plot_convergence import plot_convergence


obj = CampusStationObjective(
    "data/demand_points.csv"
)

de = DERand1Bin(
    objective=obj,
    bounds=[
        (0,50),
        (0,30)
    ],
    pop_size=20
)

best_solution, best_fitness, history = (
    de.optimize(
        generations=50,
        F=0.5,
        CR=0.9
    )
)

print("\nBest Solution:")

print(best_solution)

print("\nBest Fitness:")

print(best_fitness)

# 绘制DE/rand/1/bin收敛曲线
plot_convergence(history)