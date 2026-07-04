from src.objective import CampusStationObjective
from src.de_rand_1_bin import DERand1Bin


obj = CampusStationObjective(
    "data/demand_points.csv"
)

de = DERand1Bin(
    objective=obj,
    bounds=[
        (0,50),
        (0,30)
    ],
    pop_size=10
)

de.initialize_population()

idx = 0

target = de.population[idx]

print("Before:")

print(target)

print(
    de.fitness[idx]
)

mutant = de.mutation(idx)

trial = de.crossover(
    target,
    mutant
)

de.selection(
    idx,
    trial
)

print()

print("After:")

print(
    de.population[idx]
)

print(
    de.fitness[idx]
)