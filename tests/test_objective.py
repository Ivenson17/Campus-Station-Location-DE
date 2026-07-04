from src.objective import CampusStationObjective


obj = CampusStationObjective(
    "data/demand_points.csv"
)

fitness = obj.evaluate([25, 18])

print("fitness =", fitness)