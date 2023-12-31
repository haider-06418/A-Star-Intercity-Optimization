# file for testing and debugging

import json

# function to load json file into a dictionary
def load_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data

graph = load_json("updated_graph.json")

# with open('graph/graph_updated.json', 'w') as file:
#     json.dump(graph, file, indent=4)

import heapq

def heuristic(graph, start, goal):
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        (cost, current_node) = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            print(f'Distance from {start} -> {goal}: {cost}')
            return cost

        for neighbor in graph[current_node]:
            neighbor_city = neighbor['city']
            neighbor_cost = neighbor['distance']
            total_cost = cost + neighbor_cost
            heapq.heappush(priority_queue, (total_cost, neighbor_city))

    return float('inf')  # Indicates that there is no path between start and goal



# start_city = "Karachi"
# start_city = "Islamabad"
# goal_city = "Khanewal"
# goal_city = "Muzaffarabad"

# start_city = "Jhelum"
# goal_city = "Islamabad"

# graph_file = "graph/graph_reduced.json"
# graph = load_json(graph_file)


# print(graph['Jhelum'])

# print(heuristic(graph, start_city, goal_city))

# heuristic(graph, start_city, goal_city)

sum_astar = 0

sum_astar += heuristic(graph, "Karachi", "Khanewal")
heuristic(graph, "Khanewal", "Islamabad")
sum_astar += heuristic(graph, "Khanewal", "Jhang")
sum_astar += heuristic(graph, "Jhang", "Sargodha")
sum_astar += heuristic(graph, "Sargodha", "Jhelum")
sum_astar += heuristic(graph, "Jhelum", "Islamabad")

print(sum_astar)

print('')

sum_djkistra = 0


sum_djkistra += heuristic(graph, "Karachi", "Khanewal")
heuristic(graph, 'Khanewal', 'Islamabad')
sum_djkistra += heuristic(graph, 'Khanewal', 'Toba Tek Singh')
sum_djkistra += heuristic(graph, 'Toba Tek Singh', 'Chiniot')
sum_djkistra += heuristic(graph, 'Chiniot', 'Mandi Bahauddin')
sum_djkistra += heuristic(graph, 'Mandi Bahauddin', 'Islamabad')

print(sum_djkistra)


# testing best first
import json
import time
from bestfs import best_first_search
def load_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data

graph = load_json('graphs/graph_updated.json')

# start_city = "Karachi"
# goal_city = "Mirpur Khas"

# start_city = "Jhelum"
# goal_city = "Gwadar"

start_city = "Gujrat"
goal_city = "Gilgit"


# best first search
start_time = time.time()
path_3, cost_3, no_of_nodes_explored = best_first_search(graph, start_city, goal_city)
end_time = time.time()
time_taken = end_time - start_time
print('BestFS:')
if path_3:
    print(f"Path from {start_city} to {goal_city}:")
    print(" -> ".join(path_3))
    print(f"Total Cost: {cost_3}")
    print(f"Number of nodes explored: {no_of_nodes_explored}")
    print(f"Time taken: {time_taken} seconds")
else:
    print(f"No path found from {start_city} to {goal_city}.")
print(' ')