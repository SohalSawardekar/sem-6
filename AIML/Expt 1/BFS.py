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

    def retrace_path(self, parent, goal_node):
        path = []
        current_node = goal_node
        while current_node is not None:
            path.append(current_node)
            current_node = parent.get(current_node, None)
        path.reverse() 
        return path

    def bfs(self, start, goal_node):
        if start not in self.graph:
            return [], []  

        visited = set()
        queue = deque([start])
        order = []
        parent = {start: None}  

        while queue:
            node = queue.popleft()

            if node not in visited:
                visited.add(node)
                order.append(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)
                        parent[neighbor] = node

        if goal_node in parent:
            path = self.retrace_path(parent, goal_node)
        else:
            path = []  

        return order, path


if __name__ == "__main__":
    g = Graph()

    print("Enter edges (format: node1 node2). Type -1 when finished:")
    while True:
        edge = input("Edge: ")
        if edge == "-1":
            break
        try:
            node1, node2 = edge.split()
            g.add_edge(node1, node2)
        except ValueError:
            print("Invalid format! Enter the edge as 'node1 node2'.")

    start_node = input("Enter the starting node: ")
    goal_node = input("Enter the goal node: ")

    bfs_result, final_path = g.bfs(start_node, goal_node)
    if bfs_result:
        print(f"BFS Traversal from node {start_node}: {bfs_result}")
        if final_path:
            print(f"Path from node {start_node} to {goal_node}: {final_path}")
        else:
            print(f"No path found from node {start_node} to {goal_node}.")
    else:
        print(f"Node {start_node} is not in the graph.")



# Output: 

# Enter edges (format: node1 node2). Type -1 when finished:
# Edge: A B
# Edge: A C
# Edge: B D
# Edge: C F
# Edge: F E 
# Edge: B E
# Edge: -1

# Enter the starting node: A
# Enter the goal node: D

# BFS Traversal from node A: ['A', 'B', 'C', 'D', 'E', 'F']
# Path from node A to D: ['A', 'B', 'D']

