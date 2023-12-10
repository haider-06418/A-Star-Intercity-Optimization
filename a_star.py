# implementation for the A Star Search Algorithm

# adapted from: https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

import heapq

# a star search algorithm
def a_star_search(graph, start, goal):
    priority_queue = [(0, start, [])]
    visited = set()

    while priority_queue:
        (cost, current_node, path) = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)
        path = path + [current_node]

        if current_node == goal:
            return path, cost

        for neighbor in graph[current_node]:
            neighbor_city = neighbor['city']
            neighbor_cost = neighbor['distance']
            total_cost = cost + neighbor_cost
            heapq.heappush(priority_queue, (total_cost, neighbor_city, path))

    return None, None
