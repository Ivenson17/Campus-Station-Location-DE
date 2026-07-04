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

mutant = de.mutation(0)

print("Original:")
print(de.population[0])

print()

print("Mutant:")
print(mutant)