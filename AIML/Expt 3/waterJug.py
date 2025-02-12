# Water Jug Problem Using DFS

from collections import deque

class WaterJug:
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

    def solutions(self):
        x, y, target = self.jug1, self.jug2, self.target
        
        isSolutionPresent = False
        solutions = deque()
        stack = []  
        visited = set()
        stack.append((0, 0, []))  

        while stack:
            a, b, path = stack.pop()  

            if a == target or b == target:
                path.append((a, b))
                solutions.append(path)
                isSolutionPresent = True
                continue

            if (a, b) in visited:
                continue
            visited.add((a, b))
            path.append((a, b))

            moves = [
                (x, b),                                 # Filling jug 1
                (a, y),                                 # Filling jug 2
                (0, b),                                 # Empty jug 1
                (a, 0),                                 # Empty jug 2
                (min(a + b, x), max(0, a + b - x)),     # Transfer from jug 2 to jug 1
                (max(0, a + b - y), min(a + b, y))      # Transfer from jug 1 to jug 2
            ]

            for move in moves:
                if move not in visited:
                    stack.append((move[0], move[1], path.copy()))

        if not isSolutionPresent:
            print("\n...No Solution Present...\n")
            return []

        return solutions

if __name__ == "__main__":
    problem = WaterJug()
    problem.getData()
    results = problem.solutions()

    i = 1
    if results:
        for result in results:
            print(f'Solution {i}:')
            i += 1
            for step in result:
                print(step)
            print("\n")
    else:
        print("\nNo solution found.")


# Output: 

# Enter the size of Jug 1: 4
# Enter the size of Jug 2: 3
# Enter the target amount: 2

# Solution 1:
# (0, 0)
# (0, 3)
# (3, 0)
# (3, 3)
# (4, 2)


# Solution 2:
# (0, 0)
# (0, 3)
# (3, 0)
# (3, 3)
# (4, 3)
# (4, 0)
# (1, 3)
# (1, 0)
# (0, 1)
# (4, 1)
# (2, 3)

