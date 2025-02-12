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

"""
Output value: 

Node Heuristic:
S 20
A 16
B 10
C 14
D 11
E 10
J 9
G 8
H 4
I 8
K 7
F 8
L 3
M 0
-1

Edge:
S A
S B
S C
S D
A B
A E
A J
B F
E J
E K
J F
K F
C G 
C H
C D
D I
I H
G L
H L 
H M
L M
-1

Enter the starting node: S
Enter the goal node: M


"""

"""
Output: 

Enter nodes with their heuristic values (format: node weight). Type -1 to stop:
Node Heuristic: S 20
Node Heuristic: A 16
Node Heuristic: B 10
Node Heuristic: C 14
Node Heuristic: D 11
Node Heuristic: E 10
Node Heuristic: J 9
Node Heuristic: G 8
Node Heuristic: H 4
Node Heuristic: I 8
Node Heuristic: K 7
Node Heuristic: F 8
Node Heuristic: L 3
Node Heuristic: M 0
Node Heuristic: -1

Enter edges (format: node1 node2). Type -1 to stop:
Edge: S A
Edge: S B
Edge: S C
Edge: S D
Edge: A B
Edge: A E
Edge: A J
Edge: B F
Edge: E J
Edge: E K
Edge: J F
Edge: K F
Edge: C G 
Edge: C H
Edge: C D
Edge: D I
Edge: I H
Edge: G L
Edge: H L 
Edge: H M
Edge: L M
Edge: -1

Enter the starting node: S
Enter the goal node: M

Step-by-step execution of Best-First Search:

Step 1:
OPEN                           CLOSED
------------------------------ ------------------------------
('S', None, 20)


Step 2:
OPEN                           CLOSED
------------------------------ ------------------------------
('B', 'S', 10)                 ('S', None, 20)
('D', 'S', 11)
('C', 'S', 14)
('A', 'S', 16)


Step 3:
OPEN                           CLOSED
------------------------------ ------------------------------
('F', 'B', 8)                  ('S', None, 20)
('D', 'S', 11)                 ('B', 'S', 10)
('C', 'S', 14)
('A', 'S', 16)
('A', 'S', 16)


Step 4:
OPEN                           CLOSED
------------------------------ ------------------------------
('K', 'F', 7)                  ('S', None, 20)
('J', 'F', 9)                  ('B', 'S', 10)
('D', 'S', 11)                 ('F', 'B', 8)
('C', 'S', 14)
('A', 'S', 16)
('A', 'S', 16)


Step 5:
OPEN                           CLOSED
------------------------------ ------------------------------
('J', 'F', 9)                  ('S', None, 20)
('E', 'K', 10)                 ('B', 'S', 10)
('D', 'S', 11)                 ('F', 'B', 8)
('C', 'S', 14)                 ('K', 'F', 7)
('A', 'S', 16)
('A', 'S', 16)


Step 6:
OPEN                           CLOSED
------------------------------ ------------------------------
('E', 'K', 10)                 ('S', None, 20)
('E', 'K', 10)                 ('B', 'S', 10)
('D', 'S', 11)                 ('F', 'B', 8)
('C', 'S', 14)                 ('K', 'F', 7)
('A', 'S', 16)                 ('J', 'F', 9)
('A', 'S', 16)
('A', 'S', 16)


Step 7:
OPEN                           CLOSED
------------------------------ ------------------------------
('E', 'K', 10)                 ('S', None, 20)
('D', 'S', 11)                 ('B', 'S', 10)
('C', 'S', 14)                 ('F', 'B', 8)
('A', 'S', 16)                 ('K', 'F', 7)
('A', 'S', 16)                 ('J', 'F', 9)
('A', 'S', 16)                 ('E', 'K', 10)
('A', 'S', 16)


Step 8:
OPEN                           CLOSED
------------------------------ ------------------------------
('D', 'S', 11)                 ('S', None, 20)
('C', 'S', 14)                 ('B', 'S', 10)
('A', 'S', 16)                 ('F', 'B', 8)
('A', 'S', 16)                 ('K', 'F', 7)
('A', 'S', 16)                 ('J', 'F', 9)
('A', 'S', 16)                 ('E', 'K', 10)


Step 9:
OPEN                           CLOSED
------------------------------ ------------------------------
('I', 'D', 8)                  ('S', None, 20)
('C', 'S', 14)                 ('B', 'S', 10)
('C', 'S', 14)                 ('F', 'B', 8)
('A', 'S', 16)                 ('K', 'F', 7)
('A', 'S', 16)                 ('J', 'F', 9)
('A', 'S', 16)                 ('E', 'K', 10)
('A', 'S', 16)                 ('D', 'S', 11)


Step 10:
OPEN                           CLOSED
------------------------------ ------------------------------
('H', 'I', 4)                  ('S', None, 20)
('C', 'S', 14)                 ('B', 'S', 10)
('C', 'S', 14)                 ('F', 'B', 8)
('A', 'S', 16)                 ('K', 'F', 7)
('A', 'S', 16)                 ('J', 'F', 9)
('A', 'S', 16)                 ('E', 'K', 10)
('A', 'S', 16)                 ('D', 'S', 11)
                               ('I', 'D', 8)


Step 11:
OPEN                           CLOSED
------------------------------ ------------------------------
('M', 'H', 0)                  ('S', None, 20)
('L', 'H', 3)                  ('B', 'S', 10)
('C', 'S', 14)                 ('F', 'B', 8)
('C', 'S', 14)                 ('K', 'F', 7)
('C', 'S', 14)                 ('J', 'F', 9)
('A', 'S', 16)                 ('E', 'K', 10)
('A', 'S', 16)                 ('D', 'S', 11)
('A', 'S', 16)                 ('I', 'D', 8)
('A', 'S', 16)                 ('H', 'I', 4)



Best-First Search Traversal Order: ['S', 'B', 'F', 'K', 'J', 'E', 'D', 'I', 'H', 'M']
Path from S to M: ['S', 'D', 'I', 'H', 'M']

"""