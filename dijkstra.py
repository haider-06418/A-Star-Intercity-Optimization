# implementation for the Dijkstra's Algorithm

# adapted from: https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html

import heapq

# Dijkstra's Algorithm
def dijkstra_algorithm(graph, start, end):
    priority_queue = [(0, start, [])]
    visited = set()

    while priority_queue:
        (current_distance, current_city, path) = heapq.heappop(priority_queue)

        if current_city in visited:
            continue

        visited.add(current_city)
        path = path + [current_city]

        if current_city == end:
            return current_distance, path

        for neighbor in graph[current_city]:
            neighbor_city = neighbor['city']
            neighbor_distance = neighbor['distance']
            total_distance = current_distance + neighbor_distance
            heapq.heappush(priority_queue, (total_distance, neighbor_city, path))

    return float('inf'), []
