import numpy as np
import project_helpers_metrics as phm

def normalize(weights):
    """
    fix weights so it is >= 0 and add up to 1
    """
    weights = np.array(weights)
    weights[weights < 0] = 0
    total = np.sum(weights)
    if total == 0:
        return np.ones(len(weights)) / len(weights)

    weights = weights / total

    return weights

def random_portfolio(n_assets):
    """
    make one random valid split across n_assets funds
    """
    raw_weights = np.random.random(n_assets)
    return normalize(raw_weights)

def make_population(pop_size, n_assets):
    """
    creates a population for the funds
    """
    population = []
    for i in range(pop_size):
        population.append(random_portfolio(n_assets))
    return population

def fitness(weights, returns):
    """
    scores on portoflio by the sharpe ratio
    """
    port_daily = phm.portfolio_returns(weights, returns)
    sharpe_score  = phm.sharpe(port_daily)
    return sharpe_score

def select(population, scores, n_keep):
    """
    after portfolio is scored the best is kept as parents
    """
    top_pos = np.argsort(scores)[::-1][:n_keep]

    parents = []
    for top in top_pos:
        parents.append(population[top])
    return parents

def crossover(parent_a, parent_b):
    """
    takes the 2 parents and create a child that is between the parents
    """
    n_assets = len(parent_a)
    cut = np.random.randint(1, n_assets)
    child = np.concatenate((parent_a[:cut], parent_b[cut:]))
    return normalize(child) # normalizes the child stock

def mutate(weights, rate):
    """
    with a probability function takes a random fund to mutate to a new random value then normalize
    inspiration from
    https://medium.com/@Data_Aficionado_1083/genetic-algorithm-with-python-made-easy-code-easy-explanation-87c3ad6ca152
    """
    if np.random.random() >= rate:
        return weights
    
    mutated = weights.copy()
    position = np.random.randint(0,len(weights))
    mutated[position] = np.random.random()

    return normalize(mutated)

def run_ga(returns, pop_size, n_keep, generations, rate, seed):
    """
    this creates a random starting population where it keeps the best and makes a new population 
    scores the final pop and returns the best port with the best scores of the history
    relied on primary resources
    """
    #scoring
    np.random.seed(seed)
    n_assets = returns.shape[1]
    population = make_population(pop_size, n_assets)

    best_hist = []

    for gen in range(generations):
        scores = []
        for weights in population:
            scores.append(fitness(weights, returns))

        best_hist.append(float(max(scores)))

        parents = select(population, scores, n_keep)
        new_pop = list(parents)# elitism: best parents carried over unchanged

        while len(new_pop) < pop_size:
            i = np.random.randint(0, n_keep)
            j = np.random.randint(0, n_keep)
            child = crossover(parents[i], parents[j])
            child = mutate(child, rate)
            new_pop.append(child)

        population = new_pop

    final_scores = []
    for weights in population:
        final_scores.append(fitness(weights, returns))

    best_spot = np.argmax(final_scores)
    best_weights = population[best_spot]

    

    return best_weights, best_hist