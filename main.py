def longest_path(graph: list) -> int:
    topo_order = topological_sort(graph)
    return calculate_longest_path(graph, topo_order)
    pass

# Helper function to perform topological sort
def topological_sort(graph):
    from collections import deque
    
    n = len(graph)
    in_degree = [0] * n
    for u in range(n):
        for v, _ in graph[u]:
            in_degree[v] += 1
    
    queue = deque()
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
    
    topo_order = []
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v, _ in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    return topo_order
    pass

# Function to calculate longest path using topological sort
def calculate_longest_path(graph, topo_order):
    n = len(graph)
    dp = [-float('inf')] * n
    
    # Since the graph could have multiple starting points, 
    # we need to consider paths starting from any node.
    for node in topo_order:
        if dp[node] == -float('inf'):
            dp[node] = 0  # Starting point for a new path
    
    for u in topo_order:
        for v, w in graph[u]:
            if dp[u] != -float('inf') and dp[u] + w > dp[v]:
                dp[v] = dp[u] + w
    
    return max(dp)

# Example usage
if __name__ == "__main__":
    graph = [
        [(1, 3), (2, 2)],
        [(3, 4)],
        [(3, 1)],
        []
    ]
    print(longest_path(graph))  # Output: 7
    pass
