# implementation of the depth-first search algorithm (DFS)

# adapted from: https://favtutor.com/blogs/depth-first-search-python


def dfs_algorithm(graph, start, goal):
    stack = [start]
    visited = {start: None}  # Track visited nodes and paths

    while stack:
        current = stack.pop()

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = visited[current]
            return path[::-1]  # Return path in correct order

        for neighbor in graph[current]:
            if neighbor['city'] not in visited:
                visited[neighbor['city']] = current
                stack.append(neighbor['city'])

    return None  # No path found