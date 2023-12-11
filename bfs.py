# implementation of the breadth-first search algorithm (BFS)

# adapted from: https://favtutor.com/blogs/breadth-first-search-python


from collections import deque


def bfs_algorithm(graph, start, goal):
    queue = deque([start])
    visited = {start: None}  # Track visited nodes and paths

    while queue:
        current = queue.popleft()

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = visited[current]
            return path[::-1]  # Return path in correct order

        for neighbor in graph[current]:
            if neighbor['city'] not in visited:
                visited[neighbor['city']] = current
                queue.append(neighbor['city'])

    return None  # No path found