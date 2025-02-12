import heapq

class Graph:
    def __init__(self):
        self.graph = {}  # Adjacency list
        self.heuristics = {}  # Heuristic values (weights) of nodes
        self.step = 0

    def add_node(self, node, heuristicVal=0):
        """Add a node with its heuristic value."""
        if node not in self.graph:
            self.graph[node] = []
            self.heuristics[node] = int(heuristicVal)  # Store heuristic as integer

    def add_edge(self, node1, node2):
        """Create an undirected connection between two nodes."""
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)
        else:
            print(f"Error: One or both nodes ({node1}, {node2}) not found in graph.")

    def retrace_path(self, parent, goal_node):
        """Reconstruct the path from start to goal."""
        path = []
        current = goal_node
        while current is not None:
            path.append(current)
            current = parent.get(current, None)
        path.reverse()
        return path

    def heuristic(self, node):
        """Return heuristic (weight) of the node."""
        return self.heuristics.get(node, float('inf'))  # Default to infinity if node not found

    def displayStack(self, priority_queue, closed_list, parent):
        # Sort OPEN list for display (Priority Queue)
            open_list = sorted(priority_queue)
            open_formatted = [(node, parent.get(node, None), self.heuristic(node)) for _, node in open_list]

            # Print OPEN and CLOSED lists side by side
            print(f"Step {self.step}:")
            print(f"{'OPEN':<30} {'CLOSED':<30}")
            print(f"{'-'*30} {'-'*30}")

            max_length = max(len(open_formatted), len(closed_list))
            for i in range(max_length):
                open_str = f"{open_formatted[i]}" if i < len(open_formatted) else ""
                closed_str = f"{closed_list[i]}" if i < len(closed_list) else ""
                print(f"{open_str:<30} {closed_str:<30}")
            print("\n")
        
    def best_first_search(self, start, goal):
        """Perform Best-First Search using heuristic values."""
        if start not in self.graph or goal not in self.graph:
            return [], []  # If start/goal doesn't exist, return empty lists

        visited = set()
        priority_queue = [(self.heuristic(start), start)]  # Priority queue based on heuristic values
        order = []  # Nodes visited in order
        parent = {start: None}
        closed_list = []

        print("\nStep-by-step execution of Best-First Search:\n")

        while priority_queue:
            self.step += 1

            # Display the stack Table
            self.displayStack(priority_queue, closed_list, parent)

            # Pop the best node (lowest heuristic) from the OPEN list
            _, current_node = heapq.heappop(priority_queue)

            if current_node in visited:
                continue

            visited.add(current_node)
            order.append(current_node)

            # Add to CLOSED list
            closed_list.append((current_node, parent.get(current_node, None), self.heuristic(current_node)))

            if current_node == goal:
                return order, self.retrace_path(parent, goal)

            # Add neighbors to the OPEN list
            for neighbor in self.graph[current_node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (self.heuristic(neighbor), neighbor))
                    if neighbor not in parent:
                        parent[neighbor] = current_node

        return order, []  # If goal not reached, return empty path

if __name__ == "__main__":
    g = Graph()

    print("Enter nodes with their heuristic values (format: node weight). Type -1 to stop:")
    while True:
        inp = input("Node Heuristic: ").strip()
        if inp == "-1":
            break
        try:
            node, heuristicVal = inp.split()
            g.add_node(node, heuristicVal)
        except ValueError:
            print("Invalid format! Use 'node heuristic' (Example: A 10).")

    print("\nEnter edges (format: node1 node2). Type -1 to stop:")
    while True:
        edge = input("Edge: ").strip()
        if edge == "-1":
            break
        try:
            node1, node2 = edge.split()
            g.add_edge(node1, node2)
        except ValueError:
            print("Invalid format! Use 'node1 node2' (Example: A B).")

    start_node = input("\nEnter the starting node: ").strip()
    goal_node = input("Enter the goal node: ").strip()

    traversal_order, final_path = g.best_first_search(start_node, goal_node)

    if traversal_order:
        print(f"\nBest-First Search Traversal Order: {traversal_order}")
        if final_path:
            print(f"Path from {start_node} to {goal_node}: {final_path}")
        else:
            print(f"No path found from {start_node} to {goal_node}.")
    else:
        print(f"\nError: Node {start_node} is not in the graph.")
