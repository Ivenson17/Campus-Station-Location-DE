import numpy as np
import matplotlib.pyplot as plt

from src.de_rand_1_bin import DERand1Bin
from src.objective import CampusStationObjective


def run_single_F(F, runs=5):

    obj = CampusStationObjective("data/demand_points.csv")

    results = []

    for _ in range(runs):

        model = DERand1Bin(
            objective=obj,
            bounds=[(0, 50), (0, 30)],
            pop_size=20
        )

        _, fitness, _ = model.optimize(
            generations=50,
            F=F,
            CR=0.9
        )

        results.append(fitness)

    return np.mean(results)


def main():

    F_values = [0.3, 0.5, 0.7, 0.9]
    mean_fitness = []

    for F in F_values:
        print(f"Running F = {F}")
        score = run_single_F(F)
        mean_fitness.append(score)

    # ===== 画图 =====
    plt.figure(figsize=(8, 5))

    plt.plot(
        F_values,
        mean_fitness,
        marker='o',
        linewidth=2
    )

    plt.xlabel("F (Scaling Factor)")
    plt.ylabel("Mean Best Fitness")
    plt.title("Sensitivity Analysis of F in DE/rand/1/bin")

    plt.grid(True)

    plt.savefig(
        "results/sensitivity_F.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    print("\nF values:", F_values)
    print("Fitness:", mean_fitness)


if __name__ == "__main__":
    main()