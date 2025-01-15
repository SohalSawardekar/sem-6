from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}  # Initialize an empty adjacency list

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)  # Remove this line for a directed graph

    def bfs(self, start):
        if start not in self.graph:
            return []  # Return empty if the start node is not in the graph

        visited = set()         # Set to keep track of visited nodes
        queue = deque([start])  # Initialize a queue with the start node
        order = []              # List to store the BFS traversal order

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                order.append(node)
                # Add unvisited neighbors to the queue
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return order


# Main Program
if __name__ == "__main__":
    g = Graph()

    # Take user input for the graph
    print("Enter edges (format: node1 node2). Type 'done' when finished:")
    while True:
        edge = input("Edge: ")
        if edge.lower() == "done":
            break
        try:
            node1, node2 = edge.split()
            g.add_edge(node1, node2)
        except ValueError:
            print("Invalid format! Enter the edge as 'node1 node2'.")

    start_node = input("Enter the starting node for BFS: ")

    # Perform BFS and display the result
    bfs_result = g.bfs(start_node)
    if bfs_result:
        print(f"BFS starting from node {start_node}: {bfs_result}")
    else:
        print(f"Node {start_node} is not in the graph.")
