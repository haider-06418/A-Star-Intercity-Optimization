# main file

import json
import time
import matplotlib.pyplot as plt

import a_star
import dijkstra


# function to load json file into a dictionary
def load_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data

# # plotting a bar chart
# def plot_bar_chart(categories, values, title, ylabel):
#     plt.figure(figsize=(10, 6))
#     plt.bar(categories, values, color='skyblue')
#     plt.title(title)
#     plt.ylabel(ylabel)
#     plt.xticks(categories)
#     plt.show()


# # measuring performance metrics of for all algorithms for the given start and end nodes
# def measure_performance(start_node, end_node):
#     start_time = time.time()
    
#     path, cost = algorithm(start_node, end_node) 

#     end_time = time.time()

#     time_taken = end_time - start_time
#     nodes_explored = len(path)

#     return time_taken, cost, nodes_explored



# time_taken, cost, nodes_explored = measure_performance("CityA", "CityB")
# algorithms = ['A*', 'Dijkstra', 'Kruskal', 'Best First']
# execution_times = [0.5, 0.8, 0.7, 0.6]  # in seconds
# path_costs = [10, 12, 11, 13]
# nodes_explored = [50, 80, 70, 60]


# # Plotting each metric
# plot_bar_chart(algorithms, execution_times, 'Execution Time Comparison', 'Time (seconds)')
# plot_bar_chart(algorithms, path_costs, 'Path Cost Comparison', 'Cost')
# plot_bar_chart(algorithms, nodes_explored, 'Nodes Explored Comparison', 'Number of Nodes')





start_city = "Karachi"
# start_city = "Islamabad"
# goal_city = "Islamabad"
goal_city = "Muzaffarabad"

# start_city = "Jhelum"
# goal_city = "Gwadar"

graph_file = "graphs/graph_updated.json"
graph = load_json(graph_file)

# a star

print('A*')
# path, cost = a_star.a_star_search(graph, start_city, goal_city)
# path, cost = a_star_new.a_star_search(graph, start_city, goal_city)
path, cost, no_of_nodes_explored = a_star.a_star_search(graph, start_city, goal_city)

if path:
    print(f"Optimal Path from {start_city} to {goal_city}:")
    print(" -> ".join(path))
    print(f"Total Cost: {cost}")
    print(f"Number of nodes explored: {no_of_nodes_explored}")
else:
    print(f"No path found from {start_city} to {goal_city}.")


# dijkstra

print('Dijkstra')
# path, cost = dijkstra.dijkstra_algorithm(graph, start_city, goal_city)
path, cost, no_of_nodes_explored = dijkstra.dijkstra_algorithm(graph, start_city, goal_city)

if path:
    print(f"Shortest Path from {start_city} to {goal_city}:")
    print(" -> ".join(path))
    print(f"Total Cost: {cost}")
    print(f"Number of nodes explored: {no_of_nodes_explored}")
else:
    print(f"No path found from {start_city} to {goal_city}.")


def main():
    pass
