import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if current_dist > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    return distances

def find_optimal_route(graph, start, destination):
    distances = dijkstra(graph, start)
    if distances[destination] == float('inf'):
        return None
    route = []
    node = destination
    while node != start:
        route.append(node)
        neighbors = graph[node]
        min_distance = float('inf')
        next_node = None
        for neighbor, weight in neighbors.items():
            if distances[neighbor] + weight == distances[node] and distances[neighbor] < min_distance:
                next_node = neighbor
                min_distance = distances[neighbor]
        if next_node is None or next_node in route:
            return None
        node = next_node
    route.append(start)
    route.reverse()
    return route

def get_graph_from_user():
    graph = {}
    while True:
        node = input("Enter a node (or 'done' if finished): ").strip().upper()
        if node == 'DONE':
            break
        connections = {}
        while True:
            neighbor = input(f"Enter a neighbor node for '{node}' (or 'done' if finished): ").strip().upper()
            if neighbor == 'DONE':
                break
            weight = int(input(f"Enter the weight between '{node}' and '{neighbor}': "))
            connections[neighbor] = weight
        graph[node] = connections
    return graph

# Example usage
graph = get_graph_from_user()
print("Entered graph:")
print(graph)

start = input("Enter the start node: ").strip().upper()
destination = input("Enter the destination node: ").strip().upper()

optimal_route = find_optimal_route(graph, start, destination)
if optimal_route is None:
    print("No route exists.")
else:
    print("Optimal route:", optimal_route)
￼Enter
