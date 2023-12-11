# implementation of the breadth-first search algorithm (BFS)

# adapted from: https://favtutor.com/blogs/breadth-first-search-python


from collections import deque


def bfs_algorithm(graph, start, goal):
    queue = deque([start])
    visited = {start: None}  # Track visited nodes and paths
    nodes_visited = 0  # Counter for the number of visited nodes

    while queue:
        current = queue.popleft()
        nodes_visited += 1

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = visited[current]
            return path[::-1], nodes_visited  # Return path and number of nodes visited

        for neighbor in graph[current]:
            if neighbor['city'] not in visited:
                visited[neighbor['city']] = current
                queue.append(neighbor['city'])

    return None, nodes_visited  # No path found, return None for path and the number of nodes visited
