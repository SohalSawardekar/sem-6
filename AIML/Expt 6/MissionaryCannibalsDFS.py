class MissionaryCannibalDFS:
    def __init__(self):
        self.cannibals = 0
        self.missionaries = 0
        self.boat_capacity = 2  # The boat can carry a maximum of 2 people.

    def input_data(self):
        """Takes input for the number of missionaries and cannibals."""
        self.missionaries = int(input("Enter the number of missionaries: "))
        self.cannibals = int(input("Enter the number of cannibals: "))

    def is_valid_state(self, m_left, c_left, m_right, c_right):
        """Checks if a state is valid (no missionaries eaten)."""
        if (m_left < c_left and m_left > 0) or (m_right < c_right and m_right > 0):
            return False  # Missionaries outnumbered by cannibals
        if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
            return False  # Negative people count is not possible
        return True

    def dfs(self):
        """Performs Depth-First Search (DFS) to find a solution."""
        start_state = (self.missionaries, self.cannibals, "L")  # Initial state
        goal_state = (0, 0, "R")  # Goal state (all people moved to the right side)
        
        stack = [(start_state, [])]  # Stack for DFS
        visited = set()
        visited.add(start_state)
        
        # Possible boat moves: (Missionaries, Cannibals)
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  

        while stack:
            (m_left, c_left, boat), path = stack.pop()  # Pop from stack (DFS)

            if (m_left, c_left, boat) == goal_state:
                return path + [(m_left, c_left, boat)]  # Return solution path
            
            for m_move, c_move in moves:
                if boat == "L":  # Boat moves from left to right
                    new_state = (m_left - m_move, c_left - c_move, "R")
                    new_right = (self.missionaries - (m_left - m_move), self.cannibals - (c_left - c_move))
                else:  # Boat moves from right to left
                    new_state = (m_left + m_move, c_left + c_move, "L")
                    new_right = (self.missionaries - (m_left + m_move), self.cannibals - (c_left + c_move))
                
                if self.is_valid_state(new_state[0], new_state[1], new_right[0], new_right[1]) and new_state not in visited:
                    visited.add(new_state)
                    stack.append((new_state, path + [(m_left, c_left, boat)]))  # Push new state to stack

        return None  # No solution found

    def solve(self):
        """Finds and prints the solution using DFS."""
        solution = self.dfs()
        if solution:
            print("\nSolution path (DFS Traversal Order):")
            for state in solution:
                print(state)
        else:
            print("No solution found.")

if __name__ == "__main__":
    obj = MissionaryCannibalDFS()
    obj.input_data()
    obj.solve()
