class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self): 
        return len(self.queue)

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2): 
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex doesn't exist")        
        
def earliest_ancestor(ancestors, starting_node):
    # Initialize an empty Graph and assign to graph
    graph = Graph()
    # For each edge (PAIR of vertices) contained in the ancestors input...
    for pair in ancestors:
        # Add a vertex for each ancestor
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # Add an edge connecting the pair in reverse order (gotta be done this way for graph vertices to connect properly)
        graph.add_edge(pair[1], pair[0])
    # Initialize an empty Queue and assign to queue
    queue = Queue()
    # Add a [path to] the starting_node in the queue
    queue.enqueue([starting_node])
    # Create a variable for path length and set to 1 (to be used in conditionals)
    path_length = 1
    # Create a variable for earliest ancestor and set to -1 (ditto ^ changing variable)
    earliest_ancestor = -1
    # While the queue is not empty...
    while queue.size() > 0:
        # Dequeue the queue and assign to path
        path = queue.dequeue()
        # Assign the path's last vertex [-1] to farthest
        farthest = path[-1]
        # If this path is greater or equal to the stored path length *and* the farthest vertex has a smaller value than earliest ancestor
        if (len(path) >= path_length and farthest < earliest_ancestor) or len(path) > path_length: # (or current path is longer than stored length)
            # Reassign farthest to the earliest_ancestor
            earliest_ancestor = farthest
            # Reassign length of path to path_length
            path_length = len(path)
        # For each descendant of the current earliest ancestor (farthest) contained in the graph's vertices...
        for descendant in graph.vertices[farthest]: # Must be farthest to accomodate both initial assignment and conditional logic
            # Assign a path list to the newly explored path
            new_path = list(path)
            # Append each descendant to the new_path
            new_path.append(descendant)
            # Add the new path to our queue
            queue.enqueue(new_path)
        # Return the earliest ancestor (means queue is now empty)
    return earliest_ancestor
