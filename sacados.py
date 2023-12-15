import random

# List of objects with their weights and values
objects = [
    {"weight": 2, "value": 10},
    {"weight": 3, "value": 8},
    {"weight": 4, "value": 12},
    {"weight": 5, "value": 6}
]

# Knapsack capacity
capacity = 10

def generate_random_solution():
    # Generate a random solution where objects are selected or not selected
    return [random.choice([0, 1]) for _ in range(len(objects))]

def evaluate_solution(solution):
    total_value = sum(solution[i] * obj["value"] for i, obj in enumerate(objects))
    total_weight = sum(solution[i] * obj["weight"] for i, obj in enumerate(objects))
    return total_value, total_weight

def generate_neighboring_solution(solution):
    # Generate a neighboring solution by flipping the selection of a random object
    neighbor = solution.copy()
    index = random.randint(0, len(solution) - 1)
    neighbor[index] = 1 - neighbor[index]
    return neighbor

def local_search():
    current_solution = generate_random_solution()
    best_solution = current_solution[:]
    best_value, _ = evaluate_solution(best_solution)
    iterations = 0

    while iterations < 1000:  # Set a maximum number of iterations
        neighbor = generate_neighboring_solution(current_solution)
        neighbor_value, neighbor_weight = evaluate_solution(neighbor)

        if neighbor_weight <= capacity and neighbor_value > best_value:
            current_solution = neighbor[:]
            best_solution = current_solution[:]
            best_value = neighbor_value

        iterations += 1

    return best_solution

# Solve the Knapsack problem using local search
best_solution = local_search()
best_value, best_weight = evaluate_solution(best_solution)

# Print the best solution found
print("Best Solution:", best_solution)
print("Total Value:", best_value)
print("Total Weight:", best_weight)