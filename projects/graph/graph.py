"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        # If the vertex id is already listed in vertices...
        if vertex_id in self.vertices:
            print("ERROR: this vertex already exists")
        # Otherwise...
        else:
            # Assign the vertices, with vertex_id key, to a set
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        # If both vertices are in the vertices list (connected)...
        if v1 in self.vertices and v2 in self.vertices:
            # Add the (second vertex) to [first] in vertices list
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        # Return the vertex id associated with input in vertices list
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        # Create an empty queue
        q = Queue()
        # Add starting vertex_id to the queue
        q.enqueue(starting_vertex)
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # If the vertex hasn't been visited...
            if not v in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # For each neighbor, add vertex to back of queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        # Create an empty stack
        s = Stack()
        # Push starting vertex_id to the stack
        s.push(starting_vertex)
        # Create an empty set to store visited nodes
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # If the vertex has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # For each neighbor, push the vertex to top of stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        # Hint: https://docs.python-guide.org/writing/gotchas/
        # If we haven't visited the vertex yet...
        if visited is None:
            # Assign an empty set to visited
            visited = set()
        # Add the starting vertex to the visited set
        visited.add(starting_vertex)
        # Print the starting vertex
        print(starting_vertex)
        # For each neighbor in vertices, beginning with the [starting vertex]...
        for neighbor in self.vertices[starting_vertex]:
            # If the neighbor hasn't been visited yet...
            if neighbor not in visited:
                # Recursively call this function, replace starting vertex with neighbor, and pass in the visited vertices
                return self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        # Create an empty queue
        q = Queue()
        # Add a [path to] the starting vertex_id in the queue
        q.enqueue([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue, the first PATH ([0])
            path = q.dequeue()
            # GRAB THE LAST VERTEX FROM THE PATH
            vertex = path[-1]
            # CHECK IF IT'S THE TARGET
            if vertex == destination_vertex:
                # IF SO, RETURN THE PATH
                return path
            # If the vertex has not been visited...
            elif vertex not in visited:
                # Mark it as visited
                visited.add(vertex)
                # Then add A PATH TO all neighbors to the back of the queue
                for neighbor in self.vertices[vertex]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        # Create an empty stack
        s = Stack()
        # Add a [path to] the starting vertex in stack
        s.push([starting_vertex])
        # Create an empty set to store visited 
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first path
            path = s.pop()
            # Grab the last vertex from the path
            vertex = path[-1]
            # Check if it's the target
            if vertex == destination_vertex:
                # If so, return the path
                return path
            # If the vertex hasn't been visited...
            elif vertex not in visited:
                # Add the vertex to visited
                visited.add(vertex)
                # Then add a path to all neighbors
                for neighbor in self.vertices[vertex]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    s.push(new_path)

    # Added storage devices as parameters and assigned to None for defaults
    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        # If no vertices have been visited yet...
        if visited is None:
            # Assign an empty set to visited
            visited = set()
        # If no path has been explored...
        if path is None:
            # Assign an empty array to path
            path = []
        # Add the starting vertex to visited
        visited.add(starting_vertex)
        # Reassign path to include the addition of the [visited vertex]
        path = path + [starting_vertex]
        # If we've arrived to the destination vertex (equal to current)...
        if starting_vertex == destination_vertex:
            # Return the path because work is done
            return path
        # For each neighbor found in the get_neighbors method (connected to current vertex)...
        for neighbor in self.get_neighbors(starting_vertex):
            # If the neighbor hasn't been visited yet...
            if neighbor not in visited:
                # Recursively call this function with the neighbor replacing current vertex and assign to new path
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                # If there is a new path...
                if new_path: 
                    # Return said path and repeat the above logic until we locate the path to destination
                    return new_path
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('BFS: ', graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('Normal DFS: ', graph.dfs(1, 6))
    print('Recursive DFS: ', graph.dfs_recursive(1, 6))