# Using BFS 

from collections import deque

class MissionaryCannibal:
    def __init__(self):
        self.cannibals = 0
        self.missionaries = 0
        self.boat_capacity = 2  

    def input_data(self):
        self.missionaries = int(input("Enter the number of missionaries: "))
        self.cannibals = int(input("Enter the number of cannibals: "))

    def is_valid_state(self, m_left, c_left, m_right, c_right):
        if (m_left < c_left and m_left > 0) or (m_right < c_right and m_right > 0):
            return False
        if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
            return False
        return True

    def bfs(self):
        start_state = (self.missionaries, self.cannibals, "L")  
        goal_state = (0, 0, "R")  
        queue = deque([(start_state, [])])  
        visited = set()
        visited.add(start_state)
        
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  

        while queue:
            (m_left, c_left, boat), path = queue.popleft()
            
            if (m_left, c_left, boat) == goal_state:
                return path + [(m_left, c_left, boat)]
            
            for m_move, c_move in moves:
                if boat == "L":  
                    new_state = (m_left - m_move, c_left - c_move, "R")
                    new_right = (self.missionaries - (m_left - m_move), self.cannibals - (c_left - c_move))
                else:  
                    new_state = (m_left + m_move, c_left + c_move, "L")
                    new_right = (self.missionaries - (m_left + m_move), self.cannibals - (c_left + c_move))
                
                if self.is_valid_state(new_state[0], new_state[1], new_right[0], new_right[1]) and new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [(m_left, c_left, boat)]))
        
        return None  

    def solve(self):
        solution = self.bfs()
        if solution:
            print("Solution path:")
            for state in solution:
                print(state)
        else:
            print("No solution found.")

if __name__ == "__main__":
    obj = MissionaryCannibal()
    obj.input_data()
    obj.solve()

