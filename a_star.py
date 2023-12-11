# implementation for the A Star Search Algorithm

# adapted from: https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

# import heapq

# # a star search algorithm
# def a_star_search(graph, start, goal):
#     priority_queue = [(0, start, [])]
#     visited = set()

#     while priority_queue:
#         (cost, current_node, path) = heapq.heappop(priority_queue)

#         if current_node in visited:
#             continue

#         visited.add(current_node)
#         path = path + [current_node]

#         if current_node == goal:
#             return path, cost

#         for neighbor in graph[current_node]:
#             neighbor_city = neighbor['city']
#             neighbor_cost = neighbor['distance']
#             total_cost = cost + neighbor_cost
#             heapq.heappush(priority_queue, (total_cost, neighbor_city, path))

#     return None, None



import heapq
import json


# function to load json file into a dictionary
def load_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data

graph_complete = load_json("graph_complete.json")
# coordinates_graph = load_json("city_data.json")

# import math

# def haversine(lat1, lon1, lat2, lon2):
#     R = 6371  # radius of Earth in kilometers
#     dlat = math.radians(lat2 - lat1)
#     dlon = math.radians(lon2 - lon1)
#     a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
#     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
#     distance = R * c
#     return distance

# def heuristic(city, goal):
#     x1, y1 = coordinates_graph[city]
#     x2, y2 = coordinates_graph[goal]
#     distance = haversine(x1, y1, x2, y2)
#     return distance



# heuristic function
def heuristic(city_name, goal_name):
    # graph_complete = load_json("graph_complete.json")
    if city_name == goal_name:
        return 0
    for connection in graph_complete[city_name]:
        if connection['city'] == goal_name:
            return connection['distance']
    # return None


# # heuristic function
# def heuristic(graph, start, goal):
#     priority_queue = [(0, start)]
#     visited = set()

#     while priority_queue:
#         (cost, current_node) = heapq.heappop(priority_queue)

#         if current_node in visited:
#             continue

#         visited.add(current_node)

#         if current_node == goal:
#             return cost

#         for neighbor in graph[current_node]:
#             neighbor_city = neighbor['city']
#             neighbor_cost = neighbor['distance']
#             total_cost = cost + neighbor_cost
#             heapq.heappush(priority_queue, (total_cost, neighbor_city))

#     return float('inf')  # Indicates that there is no path between start and goal


# a star search algorithm


import heapq


# A* search algorithm
def a_star_search(graph, start, goal):
    priority_queue = [(0, start, [])]
    visited = set()

    while priority_queue:
        (cost, current_node, path) = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            return path + [current_node], cost

        for neighbor in graph[current_node]:
            neighbor_city = neighbor['city']
            neighbor_cost = neighbor['distance']
            # total_cost = cost + neighbor_cost + heuristic(graph, neighbor_city, goal)
            total_cost = cost + neighbor_cost + heuristic(neighbor_city, goal)
            heapq.heappush(priority_queue, (total_cost, neighbor_city, path + [current_node]))  # Create a new list

    return None, None




# def a_star_search(graph, start, goal):
#     priority_queue = [(0, start, [])]
#     visited = set()

#     while priority_queue:
#         (cost, current_node, path) = heapq.heappop(priority_queue)

#         if current_node in visited:
#             continue

#         visited.add(current_node)
#         path = path + [current_node]

#         if current_node == goal:
#             return path, cost

#         for neighbor in graph[current_node]:
#             neighbor_city = neighbor['city']
#             neighbor_cost = neighbor['distance']
#             total_cost = cost + neighbor_cost + heuristic(graph, neighbor_city, goal)  # Update with heuristic
#             heapq.heappush(priority_queue, (total_cost, neighbor_city, path))

#     return None, None




# def a_star_search(graph, start, goal):
#     def h(node):
#         return 0

#     def reconstruct_path(came_from, current):
#         total_path = [current]
#         while current in came_from:
#             current = came_from[current]
#             total_path.insert(0, current)
#         return total_path

#     open_set = {start}
#     came_from = {}
#     g_score = {node: float('inf') for node in graph}
#     g_score[start] = 0
#     f_score = {node: float('inf') for node in graph}
#     f_score[start] = h(start)

#     while open_set:
#         current = min(open_set, key=lambda node: f_score[node])
#         if current == goal:
#             return reconstruct_path(came_from, current), g_score[goal]

#         open_set.remove(current)
#         for neighbor in graph[current]:
#             tentative_g_score = g_score[current] + graph[current][neighbor]
#             if tentative_g_score < g_score[neighbor]:
#                 came_from[neighbor] = current
#                 g_score[neighbor] = tentative_g_score
#                 f_score[neighbor] = g_score[neighbor] + h(neighbor)
#                 if neighbor not in open_set:
#                     open_set.add(neighbor)

#     return None, float('inf')  # No path found
