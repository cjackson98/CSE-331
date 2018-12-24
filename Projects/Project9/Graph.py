import random


# Custom Graph error
class GraphError(Exception): pass


class Graph:
    """
    Graph Class ADT
    """

    class Edge:
        """
        Class representing an Edge in the Graph
        """
        __slots__ = ['source', 'destination']

        def __init__(self, source, destination):
            """
            DO NOT EDIT THIS METHOD!
            Class representing an Edge in a graph
            :param source: Vertex where this edge originates
            :param destination: ID of Vertex where this edge ends
            """
            self.source = source
            self.destination = destination

        def __eq__(self, other):
            return self.source == other.source and self.destination == other.destination

        def __repr__(self):
            return f"Source: {self.source} Destination: {self.destination}"

        __str__ = __repr__

    class Path:
        """
        Class representing a Path through the Graph
        """
        __slots__ = ['vertices']

        def __init__(self, vertices=[]):
            """
            DO NOT EDIT THIS METHOD!
            Class representing a path in a graph
            :param vertices: Ordered list of vertices that compose the path
            """
            self.vertices = vertices

        def __eq__(self, other):
            return self.vertices == other.vertices

        def __repr__(self):
            return f"Path: {' -> '.join([str(v) for v in self.vertices])}\n"

        __str__ = __repr__

        def add_vertex(self, vertex):
            """
            Add a Vertex id to the path
            :param vertex: Vertex id to be added
            :return: None
            """
            # vtx = Graph().Vertex(vertex)  # Generate vertex item
            self.vertices.append(vertex)  # Add vertex ID to list

        def remove_vertex(self):
            """
            Remove the most recently added Vertex id from the path.
            :return: None
            """
            if not self.is_empty():
                self.vertices.pop()

        def last_vertex(self):
            """
            Return the last Vertex id added to the path
            :return: the last vertex id added to the path or None if the path is empty
            """
            if self.is_empty():
                return None
            return self.vertices[-1]

        def is_empty(self):
            """
            Check if the path is empty
            :return: Returns true is path is empty and false if it is not
            """
            return len(self.vertices) == 0

    class Vertex:
        """
        Class representing a Vertex in the Graph
        """
        __slots__ = ['ID', 'edges', 'visited', 'fake']

        def __init__(self, ID):
            """
            Class representing a vertex in the graph
            :param ID : Unique ID of this vertex
            """
            self.edges = []
            self.ID = ID
            self.visited = False
            self.fake = False

        def __repr__(self):
            return f"Vertex: {self.ID}"

        __str__ = __repr__

        def __eq__(self, other):
            """
            DO NOT EDIT THIS METHOD
            :param other: Vertex to compare
            :return: Bool, True if same, otherwise False
            """
            if self.ID == other.ID and self.visited == other.visited:
                if self.fake == other.fake and len(self.edges) == len(other.edges):
                    edges = set((edge.source.ID, edge.destination) for edge in self.edges)
                    difference = [e for e in other.edges if (e.source.ID, e.destination) not in edges]
                    if len(difference) > 0:
                        return False
                    return True

        def add_edge(self, destination):
            """
            Adds an edge with "destination" to the Vertex
            :param destination: Destination of edge to be added
            :return: None
            """
            edge = Graph.Edge(self, destination)
            self.edges.append(edge)

        def degree(self):
            """
            Gets the degree of the Vertex
            :return: the degree (number of outgoing edges)
            """
            return len(self.edges)

        def get_edge(self, destination):
            """
            Gets the edge leading to a specified destination node.
            :param destination: destination of edge to get
            :return: the edge if found or None if not found
            """
            if len(self.edges) == 0:
                return None
            else:
                for item in self.edges:
                    if item.destination == destination:
                        return item
            return None

        def get_edges(self):
            """
            Gets a list of all edges the edges
            :return: The list of edges
            """
            return self.edges

        def set_fake(self):
            """
            Sets the vertex as fake
            :return: None
            """
            self.fake = True

        def visit(self):
            """
            Sets the vertex as visited
            :return: None
            """
            self.visited = True

    def __init__(self, size=0, connectedness=1, filename=None):
        """
        DO NOT EDIT THIS METHOD
        Construct a random DAG
        :param size: Number of vertices
        :param connectedness: Value from 0 - 1 with 1 being a fully connected graph
        :param: filename: The name of a file to use to construct the graph.
        """
        assert connectedness <= 1
        self.adj_list = {}
        self.size = size
        self.connectedness = connectedness
        self.filename = filename
        self.construct_graph()

    def __eq__(self, other):
        """
        DO NOT EDIT THIS METHOD
        Determines if 2 graphs are IDentical
        :param other: Graph Object
        :return: Bool, True if Graph objects are equal
        """
        if len(self.adj_list) == len(other.adj_list):
            for key, value in self.adj_list.items():
                if key in other.adj_list:
                    if not self.adj_list[key] == other.adj_list[key]:
                        return False
                else:
                    return False
            return True
        return False

    def generate_edges(self):
        """
        DO NOT EDIT THIS METHOD
        Generates directed edges between vertices to form a DAG
        :return: A generator object that returns a tuple of the form (source ID, destination ID)
        used to construct an edge
        """
        random.seed(10)
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if random.randrange(0, 100) <= self.connectedness * 100:
                    yield [i, j]

    def get_vertex(self, ID):
        """
        Returns the vertex with the specified id.
        If the vertex is not found, return None
        :param ID: ID of vertex to return
        :return: Returns vertex (if found) or None if not found
        """
        return self.adj_list.get(ID)

    def construct_graph(self):
        """
        Adds all edges to a graph (using adj_list). If a filename is provided, will read the file.
        Otherwise will use generate_edges. Will not accept graphs with negative or zero size.
        Will not accept graphs with a connectedness outside of the range [0,1]. Does not insert
        parallel edges. Invalid inputs will raise a GraphError.
        :return: None
        """
        if self.filename is not None:
            try:
                file = open(self.filename)
            except:
                raise GraphError
            for line in file:
                data = line.split()

                first = int(data[0])
                second = int(data[1])

                if first not in self.adj_list:
                    self.adj_list[first] = self.Vertex(first)
                if second not in self.adj_list:
                    self.adj_list[second] = self.Vertex(second)

                if not self.Vertex(first).get_edge(second):                # Don't add parallel edges
                    self.get_vertex(first).add_edge(second)                # Add edge between first and second
        else:
            if self.size <= 0:
                raise GraphError
            elif self.connectedness <= 0 or self.connectedness > 1:
                raise GraphError
            else:
                data = list(self.generate_edges())
                for item in data:
                    first = int(item[0])
                    second = int(item[1])

                    if first not in self.adj_list:
                        self.adj_list[first] = self.Vertex(first)
                    if second not in self.adj_list:
                        self.adj_list[second] = self.Vertex(second)

                    if not self.Vertex(first).get_edge(second):  # Don't add parallel edges
                        self.get_vertex(first).add_edge(second)  # Add edge between first and second

    def BFS(self, start, target):
        """
        Breadth First Search from a given start ID to a given target ID
        :param start: ID to start path at
        :param target: ID to end path at
        :return: the path found
        """
        start_vertex = self.get_vertex(start)
        target_vertex = self.get_vertex(target)

        if start_vertex is None or target_vertex is None:
            return self.Path([])

        start_vertex.visit()
        first_path = self.Path([])
        first_path.add_vertex(start)
        path_list = [first_path]
        while len(path_list) > 0:
            current_path = path_list.pop()
            current_path.last_vertex()
            last_vertex = current_path.last_vertex()
            if last_vertex == target:
                return current_path
            else:
                test = self.get_vertex(current_path.last_vertex())
                for edge in test.edges:
                    path_list.append(Graph.Path(current_path.vertices + [edge.destination]))

    def DFS(self, start, target, path=Path()):
        """
        Depth First Search from a given start ID to a given target ID
        :param start: ID to begin searching from
        :param target: ID to search for
        :param path: path being followed
        :return: complete path
        """
        start_vertex = self.get_vertex(start)
        if start_vertex.visited is False:
            start_vertex.visit()
            path.add_vertex(start)
            edges = start_vertex.get_edges()
            for edge in edges:
                self.DFS(edge.destination, target, path)
                last_vertex = path.last_vertex()
                if edge.destination == target or last_vertex == target:
                    return path
            if path.last_vertex() != target:
                path.remove_vertex()


def fake_emails(graph, mark_fake=False):

    def check_fake_emails(start, emails=list()):

        start_vertex = graph.get_vertex(start)
        start_vertex.visit()
        edges = start_vertex.get_edges()
        deg = start_vertex.degree()

        if deg == 0:
            start_vertex.fake = True
            if start_vertex.ID not in emails:
                emails.append(start_vertex.ID)

        for edge in edges[:]:
            vertex = graph.get_vertex(edge.destination)
            deg = vertex.degree()

            if vertex.visited is False:
                check_fake_emails(edge.destination, emails)

            if vertex.fake is True:
                # vertex.fake = True
                edge.source.edges.remove(edge)

    emails = list()
    for item in graph.adj_list:
        vertex = graph.get_vertex(item)
        if vertex.visited is False:
            check_fake_emails(item, emails)

    return emails
