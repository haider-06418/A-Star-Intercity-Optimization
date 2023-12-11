# # implementation of the best first search algorithm (bestfs)

# # adapted from: https://www.geeksforgeeks.org/best-first-search-informed-search/


# from queue import PriorityQueue


# # Heuristic function that estimates the cost from the current node to the goal node.
# # Uses the smallest distance from the current node to the goal node among the available edges.
# def heuristic(node, goal, graph):
#     if node == goal:
#         return 0
#     min_distance = float('inf')
#     for neighbor in graph.get(node, []):
#         if neighbor['city'] == goal:
#             return neighbor['distance']
#         min_distance = min(min_distance, neighbor['distance'])
#     return min_distance


# def best_first_search(graph, start, goal):
#     open_list = PriorityQueue()
#     open_list.put((heuristic(start, goal, graph), start))
#     came_from = {}
#     cost_so_far = {start: 0}
#     nodes_explored = 0

#     while not open_list.empty():
#         current = open_list.get()[1]
#         nodes_explored += 1

#         if current == goal:
#             path = []
#             while current in came_from:
#                 path.append(current)
#                 current = came_from[current]
#             path.append(start)
#             return path[::-1], cost_so_far[goal], nodes_explored

#         for neighbor in graph[current]:
#             if neighbor['city'] not in came_from:
#                 new_cost = cost_so_far[current] + neighbor['distance']
#                 cost_so_far[neighbor['city']] = new_cost
#                 priority = heuristic(neighbor['city'], goal, graph)
#                 open_list.put((priority, neighbor['city']))
#                 came_from[neighbor['city']] = current

#     return None, None, nodes_explored


from queue import PriorityQueue

def heuristic(node, goal, graph):
    if node == goal:
        return 0
    min_distance = float('inf')
    for neighbor in graph.get(node, []):
        if neighbor['city'] == goal:
            return neighbor['distance']
        min_distance = min(min_distance, neighbor['distance'])
    return min_distance


def best_first_search(graph, start, goal):
    open_list = PriorityQueue()
    open_list.put((heuristic(start, goal, graph), start))
    came_from = {}
    cost_so_far = {start: 0}
    nodes_explored = 0

    while not open_list.empty():
        current = open_list.get()[1]
        nodes_explored += 1

        # print("Current node:", current)
        # print("Nodes explored:", nodes_explored)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]

                came_from.pop(current)
            path.append(start)

            return path[::-1], cost_so_far[goal], nodes_explored

        for neighbor in graph[current]:
            if neighbor['city'] not in came_from:
                new_cost = cost_so_far[current] + neighbor['distance']
                cost_so_far[neighbor['city']] = new_cost
                priority = heuristic(neighbor['city'], goal, graph)
                open_list.put((priority, neighbor['city']))
                came_from[neighbor['city']] = current

        # for neighbor in graph[current]:
        #     if neighbor['city'] == goal:
        #         # If the neighbor is the goal, return the path immediately
        #         path = [goal, current]
        #         while current in came_from:
        #             current = came_from[current]
        #             path.append(current)
        #         return path[::-1], cost_so_far[goal], nodes_explored

        #     if neighbor['city'] not in came_from:
        #         new_cost = cost_so_far[current] + neighbor['distance']
        #         cost_so_far[neighbor['city']] = new_cost
        #         priority = heuristic(neighbor['city'], goal, graph)
        #         open_list.put((priority, neighbor['city']))
        #         came_from[neighbor['city']] = current


    return None, None, nodes_explored

# Example usage
# graph = {
#     'A': [{'city': 'B', 'distance': 1}, {'city': 'C', 'distance': 2}],
#     'B': [{'city': 'D', 'distance': 3}],
#     'C': [{'city': 'D', 'distance': 2}],
#     'D': [{'city': 'E', 'distance': 4}],
#     'E': [{'city': 'F', 'distance': 1}],
#     'F': []
# }

# import json 
# def load_json(json_file):
#     with open(json_file, 'r') as file:
#         data = json.load(file)
#     return data

# graph = load_json('graphs/graph_updated.json')
# # graph = load_json('graph/graph_reduced.json')

# start_node = 'Karachi'
# goal_node = 'Islamabad'
# result = best_first_search(graph, start_node, goal_node)

# print("Result:", result)
