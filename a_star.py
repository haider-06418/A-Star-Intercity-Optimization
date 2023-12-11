# implementation for the A Star Search Algorithm

# adapted from: https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2


from queue import PriorityQueue


# Heuristic function that estimates the cost from the current node to the goal node.
# Uses the smallest distance from the current node to the goal node among the available edges.    
def heuristic(node, goal, graph):
    if node == goal:
        return 0
    min_distance = float('inf')
    for neighbor in graph.get(node, []):
        if neighbor['city'] == goal:
            return neighbor['distance']
        min_distance = min(min_distance, neighbor['distance'])
    return min_distance


def a_star_search(graph, start, goal):
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
                priority = new_cost + heuristic(neighbor['city'], goal, graph)
                open_list.put((priority, neighbor['city']))
                came_from[neighbor['city']] = current

    return None, None, None
