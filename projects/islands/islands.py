class Stack():
    def __init__(self):
        # Stack is always an empty array upon initialization
        self.stack = []
    def push(self, value):
        # To push, call append on the stack and pass in a value
        self.stack.append(value)
    def pop(self):
        # If our stack has a size greater than 0...
        if self.size() > 0:
            # Return the result of calling pop on the stack (no need for value)
            return self.stack.pop()
        # Otherwise...
        else:
            # It's empty, so return None
            return None
    def size(self): 
        return len(self.stack)

def island_counter(matrix):
    # Create an empty array and assign to visited
    visited = []
    # For each index in the range of our matrix's length (column in this case)...
    for i in range(len(matrix)):
        # Preallocate (append) the visited array with [False] * length of matrix row [0]
        visited.append([False] * len(matrix[0]))
    # Initialize an island_count variable and assign 0
    island_count = 0
    # For each cell in the matrix (start with columns in range of row length)...
    for col in range(len(matrix[0])): # matrix[0] means first row
        # For each cell in the matrix (rows in range of column height)...
        for row in range(len(matrix)): # len(matrix) means first column
            # If this cell has not been visited...
            if not visited[row][col]: # always reverse the order!
                # If we reach a cell with value 1 (potential island)...
                if matrix[row][col] == 1:
                    # Do a depth first traversal and mark each 1 as visited
                    visited = dft(col, row, matrix, visited)
                    # Increment the island_count by 1
                    island_count += 1
                # Otherwise, there's no way it can be an island...
                else:
                    # Assign True to the visited cell so we can check off list
                    visited[row][col] = True
    # After all the loops and conditionals complete their tests, return island count
    return island_count

def dft(col, row, matrix, visited):
    # Initialize an empty stack and assign to s
    s = Stack()
    # Push the starting node's (column, row) onto the stack
    s.push((col, row))
    # While the stack isn't empty...
    while s.size() > 0:
        # Pop the node/vertex from top of the stack
        v = s.pop()
        # Assign first index to col
        col = v[0]
        # Assign second index to row
        row = v[1]
        # If this [particular][cel] hasn't been visited...
        if not visited[row][col]:
            # Assign True to mark the cel as visited
            visited[row][col] = True
            # For each (neighboring, cel) within our matrix...
            for neighbor in get_neighbors((col, row), matrix): 
                # Push each neighbor to the top of our stack
                s.push(neighbor)
    # After the loops and condionals complete their tests, return visited
    return visited
    # Result gets fed into island_counter conditonal that's checking for 1's

def get_neighbors(vertex, graph_matrix):
    # Assign first part of vertex to col
    col = vertex[0]
    # Assign second part to row
    row = vertex[1]
    # Initialize neighbors variable with an empty array
    neighbors = []
    # If we're not in the top row (0) and the cell above equals 1...
    if row > 0 and graph_matrix[row - 1][col] == 1:
        # Append the the northern cell into neighbors (order, reversed)
        neighbors.append((col, row - 1))
    # If we're not in the bottom row and the cell below equals 1...
    if row < len(graph_matrix) - 1 and graph_matrix[row + 1][col] == 1:
        # Append the southern cell into neighbors
        neighbors.append((col, row + 1))
    # If we're not in the last[cell] and the right cell equals 1...
    if col < len(graph_matrix[0]) - 1 and graph_matrix[row][col + 1] == 1:
        # Append the eastern cell into neighbors
        neighbors.append((col + 1, row))
    # If we're not in first cell (0) and the left cell equals 1...
    if col > 0 and graph_matrix[row][col - 1] == 1:
        # Append the western cell into neighbors
        neighbors.append((col - 1, row))
    # After all the conditionals are complete, return neighbors
    return neighbors
    # Result gets fed into DFT loop that tracks visited nodes

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0],
           [0, 0, 0, 0, 0]]


moreIslands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

print(island_counter(islands))
print(island_counter(moreIslands))