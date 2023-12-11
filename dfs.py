# implementation of the depth-first search algorithm (DFS)

# adapted from: https://favtutor.com/blogs/depth-first-search-python


def dfs_algorithm(graph, start, goal):
    stack = [start]
    visited = {start: None}  # Track visited nodes and paths
    nodes_visited = 0  # Counter for the number of visited nodes

    while stack:
        current = stack.pop()
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
                stack.append(neighbor['city'])

    return None, nodes_visited  # No path found, return None for path and the number of nodes visited
