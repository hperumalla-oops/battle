import copy

# Goal state
GOAL_STATE = [[1,2,3],[4,5,6],[7,8," "]]

def string_to_grid(state):
    """Convert input string to 3x3 grid."""
    grid = []
    for i in range(0, 9, 3):
        row = [int(c) if c != '0' else " " for c in state[i:i+3]]
        grid.append(row)
    return grid

def print_grid(grid):
    """Print the grid in a formatted way."""
    for row in grid:
        print(" | ".join(str(num) for num in row))
        print("-" * 9)

def find_blank(grid):
    """Find the position of the blank space."""
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                return i, j
    return None

def get_possible_moves(row, col):
    """Get possible moves for the blank space."""
    moves = [
        (row-1, col),  # Up
        (row+1, col),  # Down
        (row, col-1),  # Left
        (row, col+1)   # Right
    ]
    return [(r, c) for r, c in moves if 0 <= r < 3 and 0 <= c < 3]

def heuristic(grid):
    """Calculate the number of misplaced tiles."""
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if grid[i][j] != GOAL_STATE[i][j] and grid[i][j] != " ":
                misplaced += 1
    return misplaced

def grid_to_tuple(grid):
    """Convert grid to a hashable tuple representation."""
    return tuple(tuple(row) for row in grid)

def solve_puzzle(initial_grid):
    """Solve the 8-puzzle using A* algorithm."""
    # Open set tracks states to explore, with (state, g_cost, f_cost, parent)
    open_set = {grid_to_tuple(initial_grid): (initial_grid, 0, heuristic(initial_grid), None)}
    closed_set = set()

    while open_set:
        # Get the state with the lowest f_cost
        current_tuple = min(open_set, key=lambda x: open_set[x][2])
        current_grid, g_cost, f_cost, parent = open_set[current_tuple]

        # Check if goal is reached
        if current_grid == GOAL_STATE:
            # Reconstruct path
            path = []
            while current_grid is not None:
                path.append(current_grid)
                current_tuple = grid_to_tuple(current_grid)
                _, _, _, current_grid = open_set.get(current_tuple, (None, None, None, parent))
            return list(reversed(path))

        # Move current state to closed set
        del open_set[current_tuple]
        closed_set.add(current_tuple)

        # Find blank space
        blank_row, blank_col = find_blank(current_grid)

        # Generate possible moves
        for move_row, move_col in get_possible_moves(blank_row, blank_col):
            # Create a new grid by swapping blank space
            new_grid = copy.deepcopy(current_grid)
            new_grid[blank_row][blank_col], new_grid[move_row][move_col] = \
                new_grid[move_row][move_col], new_grid[blank_row][blank_col]

            new_tuple = grid_to_tuple(new_grid)

            # Skip if already explored
            if new_tuple in closed_set:
                continue

            # Calculate new costs
            new_g_cost = g_cost + 1
            new_f_cost = new_g_cost + heuristic(new_grid)

            # Check if this path is better or state is new
            if new_tuple not in open_set or new_f_cost < open_set[new_tuple][2]:
                open_set[new_tuple] = (new_grid, new_g_cost, new_f_cost, current_grid)

    return None  # No solution found

def main():
    # Get input from user
    state_input = input("Enter the initial state (9 digits, use 0 for blank): ")
    initial_grid = string_to_grid(state_input)

    # Solve the puzzle
    solution = solve_puzzle(initial_grid)

    if solution:
        print("\nSolution found in {} steps:".format(len(solution) - 1))
        for step, grid in enumerate(solution):
            print(f"\nStep {step}:")
            print_grid(grid)
    else:
        print("No solution exists for this puzzle.")

if __name__ == "__main__":
    mnew() 
