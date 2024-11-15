import heapq


# Distance Vector Routing Algorithm
def distance_vector_routing(graph, source):
    distances = {node: float("inf") for node in graph}
    distances[source] = 0
    routing_table = {node: source if node != source else None for node in graph}

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    routing_table[neighbor] = node

    print(f"\nDistance Vector Routing Results (Source: {source})")
    print("Routing Table:", routing_table)
    print("Distances:", distances)


# Link State Routing Algorithm
def link_state_routing(graph, source):
    distances = {node: float("inf") for node in graph}
    distances[source] = 0
    pq = [(0, source)]  # (distance, node)
    previous_nodes = {node: None for node in graph}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    print(f"\nLink State Routing Results (Source: {source})")
    print("Shortest Distances:", distances)
    print("Previous Nodes (Path):", previous_nodes)


# Function to get graph input from user
def get_graph_input():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    print("Enter the edges in the format: node1 node2 weight")
    for _ in range(num_nodes):
        node = input(f"Enter name of node {_ + 1}: ")
        graph[node] = {}
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        node1, node2, weight = input("Edge: ").split()
        weight = int(weight)
        graph[node1][node2] = weight
        graph[node2][node1] = weight  # Assuming undirected graph
    return graph


# Main function
def main():
    print("Routing Algorithm Simulation")
    print("1. Distance Vector Routing")
    print("2. Link State Routing")
    choice = int(input("Choose an algorithm (1 or 2): "))

    graph = get_graph_input()
    source_node = input("Enter the source node: ")

    if choice == 1:
        distance_vector_routing(graph, source_node)
    elif choice == 2:
        link_state_routing(graph, source_node)
    else:
        print("Invalid choice. Please select 1 or 2.")


# Run the program
if __name__ == "__main__":
    main()
