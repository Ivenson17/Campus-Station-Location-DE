📌 Campus Station Location Optimization using Differential Evolution


🚀 Project Overview
This project solves the campus parcel station location optimization problem using Differential Evolution (DE) algorithms.

We model the problem as a weighted geometric median problem and compare two DE variants:
DE/rand/1/bin
DE/current-to-best/1/bin


📊 Features
✔ Optimization using Differential Evolution
✔ Two algorithm variants comparison
✔ Convergence analysis
✔ Stability analysis (20 runs)
✔ Visualization of results

📁 Project Structure
src/
  de_rand_1_bin.py
  de_current_to_best_1_bin.py
  objective.py
  visualization.py

data/
  demand_points.csv

results/
  convergence_compare.png
  boxplot.png
  best_location.png


🚀 Run Project
python -m src.run_visualization


📈 Results
Best fitness ≈ 17483.44
Current-to-best converges faster
Rand version more exploratory


👨‍💻 Author
张栋兴