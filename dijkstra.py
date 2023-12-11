# implementation for the Dijkstra's Algorithm

# adapted from: https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html

# import heapq

# # Dijkstra's Algorithm
# def dijkstra_algorithm(graph, start, end):
#     priority_queue = [(0, start, [])]
#     visited = set()

#     while priority_queue:
#         (current_distance, current_city, path) = heapq.heappop(priority_queue)

#         if current_city in visited:
#             continue

#         visited.add(current_city)
#         path = path + [current_city]

#         if current_city == end:
#             return current_distance, path

#         for neighbor in graph[current_city]:
#             neighbor_city = neighbor['city']
#             neighbor_distance = neighbor['distance']
#             total_distance = current_distance + neighbor_distance
#             heapq.heappush(priority_queue, (total_distance, neighbor_city, path))

#     return float('inf'), []


from queue import PriorityQueue

# def dijkstra_algorithm(graph, start, goal):
#     """
#     Dijkstra's algorithm implementation.
#     """
#     # Initialize the open list with the start node and the closed list as empty
#     open_list = PriorityQueue()
#     open_list.put((0, start))
#     came_from = {}  # Track the path
#     cost_so_far = {start: 0}  # Cost from start to the node

#     while not open_list.empty():
#         # Get the current node with the lowest cost
#         current = open_list.get()[1]

#         # If the goal is reached, reconstruct and return the path
#         if current == goal:
#             path = []
#             while current in came_from:
#                 path.append(current)
#                 current = came_from[current]
#             path.append(start)
#             return path[::-1], cost_so_far[goal]  # Path and cost

#         # Explore neighbors
#         for neighbor in graph[current]:
#             new_cost = cost_so_far[current] + neighbor['distance']
#             if neighbor['city'] not in cost_so_far or new_cost < cost_so_far[neighbor['city']]:
#                 cost_so_far[neighbor['city']] = new_cost
#                 open_list.put((new_cost, neighbor['city']))
#                 came_from[neighbor['city']] = current

#     return None, None  # Return None if there is no path to the goal


def dijkstra_algorithm(graph, start, goal):
    open_list = PriorityQueue()
    open_list.put((0, start))
    came_from = {}
    cost_so_far = {start: 0}
    nodes_explored = 0

    while not open_list.empty():
        current = open_list.get()[1]
        nodes_explored += 1

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], cost_so_far[goal], nodes_explored

        for neighbor in graph[current]:
            new_cost = cost_so_far[current] + neighbor['distance']
            if neighbor['city'] not in cost_so_far or new_cost < cost_so_far[neighbor['city']]:
                cost_so_far[neighbor['city']] = new_cost
                open_list.put((new_cost, neighbor['city']))
                came_from[neighbor['city']] = current

    return None, None, None


# # Example usage of the Dijkstra algorithm
# start_city = 'Karachi'
# goal_city = 'Lahore'
# path, cost = dijkstra_search(graph_data, start_city, goal_city)
# path, cost
