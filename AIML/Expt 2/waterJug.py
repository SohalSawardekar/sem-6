from collections import deque
from math import gcd


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
        
        isSolution = False
        solutions = deque()
        visited = set()
        queue = deque()
        states = deque()
        queue.append((0, 0, [])) 
        states.append((0, 0)) 

        while queue:
            a, b, path = queue.popleft()

            if a == target or b == target:
                path.append((a, b))
                solutions.append(path)
                isSolution = True
                continue
                

            if (a, b) in visited:
                continue
            visited.add((a, b))

            path.append((a, b))

            moves = [
                (x, b),  
                (a, y),  
                (0, b),  
                (a, 0),  
                (min(a + b, x), max(0, a + b - x)),  
                (max(0, a + b - y), min(a + b, y))   
            ]

            for move in moves:
                if move not in visited:
                    queue.append((move[0], move[1], path.copy()))
                    states.append((move[0], move[1]))
            
        if(isSolution == False):
            print("...No Solution Present...")
            exit()
        
        return solutions

if __name__ == "__main__":
    problem = WaterJug()
    problem.getData()
    results = problem.solutions()

    i = 1
    print("\n")
    for result in results:
        print(f'Solution {i}: ')
        i += 1
        for set in result:
            print(set)
        print("\n")
    print("\n")
