import numpy as np
import pandas as pd

from src.de_rand_1_bin import DERand1Bin
from src.de_current_to_best_1_bin import DECurrentToBest1Bin
from src.objective import CampusStationObjective


def run_experiment(model_class, name, runs=20):

    results = []
    histories = []

    obj = CampusStationObjective("data/demand_points.csv")

    for i in range(runs):

        model = model_class(
            objective=obj,
            bounds=[(0, 50), (0, 30)],
            pop_size=20
        )

        best, fitness, history = model.optimize(
            generations=50,
            F=0.5,
            CR=0.9
        )

        results.append(fitness)
        histories.append(history)

        print(f"{name} Run {i+1}: {fitness:.4f}")

    results = np.array(results)

    summary = {
        "algorithm": name,
        "best": np.min(results),
        "worst": np.max(results),
        "mean": np.mean(results),
        "std": np.std(results)
    }

    return summary, results, histories


if __name__ == "__main__":

    rand_summary, rand_results = run_experiment(
        DERand1Bin,
        "DE/rand/1/bin"
    )

    ctbest_summary, ctbest_results = run_experiment(
        DECurrentToBest1Bin,
        "DE/current-to-best/1/bin"
    )

    df = pd.DataFrame([
        rand_summary,
        ctbest_summary
    ])

    print("\n===== Summary =====")
    print(df)

    df.to_csv("results/experiment_summary.csv", index=False)