# Water Jug Problem Using BFS

from collections import deque

class WaterJugBFS:
    def __init__(self):
        self.jug1 = 0
        self.jug2 = 0
        self.target = 0

    def getData(self):
        try:
            self.jug1 = int(input("Enter the size of Jug 1: "))
            self.jug2 = int(input("Enter the size of Jug 2: "))
            self.target = int(input("Enter the target amount: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            self.getData()

    def bfs_solutions(self):
        x, y, target = self.jug1, self.jug2, self.target
        
        queue = deque()
        queue.append((0, 0, [])) 
        visited = set()
        solutions = []

        while queue:
            a, b, path = queue.popleft()  

            if a == target or b == target:
                path.append((a, b))
                solutions.append(path)
                continue  

            if (a, b) in visited:
                continue
            visited.add((a, b))
            path.append((a, b))

            moves = [
                (x, b),                                 # Fill Jug 1
                (a, y),                                 # Fill Jug 2
                (0, b),                                 # Empty Jug 1
                (a, 0),                                 # Empty Jug 2
                (min(a + b, x), max(0, a + b - x)),     # Pour Jug 2 → Jug 1
                (max(0, a + b - y), min(a + b, y))      # Pour Jug 1 → Jug 2
            ]

            for move in moves:
                if move not in visited:
                    queue.append((move[0], move[1], path.copy()))

        if not solutions:
            print("\n...No Solution Present...\n")
        return solutions

if __name__ == "__main__":
    problem = WaterJugBFS()
    problem.getData()
    results = problem.bfs_solutions()

    if results:
        i = 1
        for result in results:
            print(f'\nSolution {i}:')
            i += 1
            for step in result:
                print(step)
        print("\nTotal solutions found:", len(results))
    else:
        print("\nNo solution found.")
