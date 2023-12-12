# implementation of the best first search algorithm (bestfs)

# adapted from: https://www.geeksforgeeks.org/best-first-search-informed-search/


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

    return None, None, nodes_explored
