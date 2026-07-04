import numpy as np


class DECurrentToBest1Bin:

    def __init__(
        self,
        objective,
        bounds,
        pop_size=20
    ):

        self.objective = objective

        # 范围
        self.bounds = bounds

        # 参数1--种群N
        self.pop_size = pop_size

        # 维度
        self.dimension = len(bounds)

        self.population = None

        self.fitness = None


    # 初始化种群
    def initialize_population(self):

        population = []

        for _ in range(self.pop_size):

            individual = []

            for lower, upper in self.bounds:
                value = np.random.uniform(
                    lower,
                    upper
                )
                individual.append(value)

            population.append(individual)

        self.population = np.array(population)

        self.fitness = np.array([
            self.objective(ind)
            for ind in self.population
        ])


    # 越界处理
    def ensure_bounds(self, vector):

        bounded = np.copy(vector)

        for j in range(self.dimension):

            lower, upper = self.bounds[j]

            bounded[j] = np.clip(
                bounded[j],
                lower,
                upper
            )

        return bounded


    # 变异(改进版)
    def mutation(self, idx, F=0.5):

        x_i = self.population[idx]

        best_idx = np.argmin(self.fitness)
        x_best = self.population[best_idx]

        candidates = list(range(self.pop_size))
        candidates.remove(idx)

        r1, r2 = np.random.choice(candidates, 2, replace=False)

        mutant = (
            x_i + F * (x_best - x_i) + F * (self.population[r1] - self.population[r2])
        )

        return self.ensure_bounds(mutant)
    

    # 交叉
    def crossover(
        self,
        target,
        mutant,
        CR=0.9
    ):

        trial = np.copy(target)

        j_rand = np.random.randint( self.dimension )

        for j in range(self.dimension):

            if ( np.random.rand() < CR or j == j_rand ):

                trial[j] = mutant[j]

        return trial
    

    # 选择
    def selection(
        self,
        idx,
        trial
    ):

        trial_fitness = self.objective( trial )

        # 比较 x_i&u_i
        if ( trial_fitness < self.fitness[idx] ):
            self.population[idx] = trial
            self.fitness[idx] = trial_fitness

    
    def evolve_one_generation(
        self,
        F=0.5,
        CR=0.9
    ):

        # 遍历(x_i ~ x_pop_size)
        for i in range(self.pop_size):

            target = self.population[i]

            # 变异
            mutant = self.mutation( i, F=F )

            # 交叉
            trial = self.crossover(
                target,
                mutant,
                CR=CR
            )

            # 选择
            self.selection( i, trial )

    
    # 获取当前最优个体
    def get_best(self):

        best_idx = np.argmin( self.fitness )

        return (
            self.population[best_idx],
            self.fitness[best_idx]
        )
    

    # optimize
    def optimize(
        self,
        generations=100,
        F=0.5,
        CR=0.9
    ):

        self.initialize_population()

        history = []

        for g in range(generations):

            self.evolve_one_generation( F=F, CR=CR )

            best_solution, best_fitness = (
                self.get_best()
            )

            history.append( best_fitness )

            print(
                f"Generation {g+1}: "
                f"{best_fitness:.2f}"
            )

        return (
            best_solution,
            best_fitness,
            history
        )