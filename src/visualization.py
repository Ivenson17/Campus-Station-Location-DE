import numpy as np
import matplotlib.pyplot as plt


# =========================
# 1. 收敛曲线对比
# =========================
def plot_convergence(rand_histories, ctbest_histories):

    plt.figure(figsize=(8, 5))

    # rand 平均
    rand_mean = np.mean(rand_histories, axis=0)
    ctbest_mean = np.mean(ctbest_histories, axis=0)

    plt.plot(rand_mean, label="DE/rand/1/bin")
    plt.plot(ctbest_mean, label="DE/current-to-best/1/bin")

    plt.xlabel("Generation")
    plt.ylabel("Best Fitness")
    plt.title("Convergence Curve Comparison")
    plt.legend()
    plt.grid(True)

    plt.savefig("results/convergence_compare.png", dpi=300)
    plt.show()


# =========================
# 2. boxplot
# =========================
def plot_boxplot(rand_results, ctbest_results):

    plt.figure(figsize=(6, 5))

    plt.boxplot([rand_results, ctbest_results])

    plt.xticks([1, 2], ["rand", "current-to-best"])

    plt.ylabel("Final Fitness")
    plt.title("Stability Comparison")

    plt.grid(True)

    plt.savefig("results/boxplot.png", dpi=300)
    plt.show()


# =========================
# 3. 最优解位置图
# =========================
def plot_solution(best_solution, df):

    plt.figure(figsize=(8, 5))

    plt.scatter(df["x"], df["y"], s=df["demand"] * 10, label="Demand Points")

    plt.scatter(best_solution[0], best_solution[1],
                c="red", s=200, label="Best Station")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Optimal Station Location")
    plt.legend()

    plt.grid(True)

    plt.savefig("results/best_location.png", dpi=300)
    plt.show()