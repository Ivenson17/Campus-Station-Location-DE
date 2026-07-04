import matplotlib.pyplot as plt

def plot_convergence(history):

    plt.figure(figsize=(8,5))

    plt.plot(
        history,
        linewidth=2
    )

    plt.xlabel("Generation")

    plt.ylabel("Best Fitness")

    plt.title(
        "DE/rand/1/bin Convergence Curve"
    )

    plt.grid(True)

    plt.savefig(
        "results/convergence_curve_rand.png",
        dpi=300,
        bbox_inches="tight"
    )