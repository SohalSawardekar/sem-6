from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}  

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)  

    def dfs_recursive(self, node, visited, order):
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in self.graph[node]:
                self.dfs_recursive(neighbor, visited, order)

    def dfs(self, start):
        """
        Iterative DFS implementation.
        """
        if start not in self.graph:
            return []  # Return empty if the start node is not in the graph

        visited = set()         # Set to keep track of visited nodes
        stack = [start]         # Stack to maintain the order of exploration
        order = []              # List to store the DFS traversal order

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                # Add unvisited neighbors to the stack
                for neighbor in reversed(self.graph[node]):
                    if neighbor not in visited:
                        stack.append(neighbor)

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

    start_node = input("Enter the starting node for DFS: ")

    # Perform DFS (iterative)
    dfs_result = g.dfs(start_node)
    if dfs_result:
        print(f"DFS (Iterative) starting from node {start_node}: {dfs_result}")
    else:
        print(f"Node {start_node} is not in the graph.")

    # Perform DFS (recursive)
    visited = set()
    order = []
    g.dfs_recursive(start_node, visited, order)
    if order:
        print(f"DFS (Recursive) starting from node {start_node}: {order}")
    else:
        print(f"Node {start_node} is not in the graph.")
