import random

def generate_board(n):
    return random.sample(range(n), n)

def calculate_conflicts(board):
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                conflicts += 1
    return conflicts

def select_parent(population, tournament_size=3):
    tournament = random.sample(population, tournament_size)
    return min(tournament, key=lambda x: calculate_conflicts(x))

def crossover(parent1, parent2):
    n = len(parent1)
    point = random.randint(1, n - 1)
    child = parent1[:point] + parent2[point:]
    return child

def mutate(board, mutation_rate=0.2):
    if random.random() < mutation_rate:
        n = len(board)
        i, j = random.sample(range(n), 2)
        board[i], board[j] = board[j], board[i]
    return board

def genetic_algorithm(n, population_size=100, max_generations=1000):
    population = [generate_board(n) for _ in range(population_size)]
    
    for generation in range(max_generations):
        population.sort(key=lambda x: calculate_conflicts(x))
        
        if calculate_conflicts(population[0]) == 0:
            return population[0], generation
        
        new_population = [population[0]]
        
        while len(new_population) < population_size:
            parent1 = select_parent(population)
            parent2 = select_parent(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        
        population = new_population
    
    return None, max_generations

def print_solution(solution):
    n = len(solution)
    for row in range(n):
        line = ['Q' if col == solution[row] else '.' for col in range(n)]
        print(' '.join(line))

if __name__ == "__main__":
    N = 8
    solution, generations = genetic_algorithm(N)
    
    if solution:
        print(f"Solution found in {generations} generations:")
        print_solution(solution)
        print("Queen positions:", solution)
    else:
        print(f"No solution found in {generations} generations.")