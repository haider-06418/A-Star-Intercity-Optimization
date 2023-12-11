# implementation for the Dijkstra's Algorithm

# adapted from: https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html


from queue import PriorityQueue


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
