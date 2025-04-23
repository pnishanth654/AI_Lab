class BlocksWorld:
    def __init__(self, initial_state):
        self.state = initial_state

    def display_state(self):
        for row in self.state:
            print(" ".join(row))
        print()

    def is_goal_state(self, goal_state):
        return self.state == goal_state

    def generate_successors(self):
        successors = []
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                if self.state[i][j] != " ":
                    if i > 0 and self.state[i - 1][j] == " ":
                        new_state = [row.copy() for row in self.state]
                        new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
                        successors.append(BlocksWorld(new_state))
                    if i < len(self.state) - 1 and self.state[i + 1][j] == " ":
                        new_state = [row.copy() for row in self.state]
                        new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
                        successors.append(BlocksWorld(new_state))
                    if j > 0 and self.state[i][j - 1] == " ":
                        new_state = [row.copy() for row in self.state]
                        new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
                        successors.append(BlocksWorld(new_state))
                    if j < len(self.state[i]) - 1 and self.state[i][j + 1] == " ":
                        new_state = [row.copy() for row in self.state]
                        new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]
                        successors.append(BlocksWorld(new_state))
        return successors

def depth_first_search(initial_state, goal_state):
    stack = [BlocksWorld(initial_state)]
    visited = set()
    step = 0
    while stack:
        current_state = stack.pop()
        if current_state.is_goal_state(goal_state):
            print(f"Goal state reached!\n")
            current_state.display_state()
            return True
        visited.add(tuple(map(tuple, current_state.state)))
        successors = current_state.generate_successors()
        for successor in successors:
            if tuple(map(tuple, successor.state)) not in visited:
                stack.append(successor)
        step += 1
        print(f"Step {step}:")
        current_state.display_state()
    print("Goal state not reachable.")
    return False

initial_state = [["A", "B", " "], ["C", " ", "D"]]
goal_state = [[" ", "B", "A"], ["C", "D", " "]]
depth_first_search(initial_state, goal_state)