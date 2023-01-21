from collections import deque


class Graph:
    """
    Graph object with functions that can link node objects with 'data' as a attribute, 'data' can be any data type.
    """
    class Node:
        """
        Creates a node object with data, parents (list with nodes connected to this node),
        paths (a list with neighbor nodes that are available as a possible node to connect to from this node),
        open (a boolean, True if node is open to be searched and visited, False if closed)
        """
        def __init__(self, data):
            self.data = data
            self.parents = []
            self.paths = []
            self.open = True

    def __init__(self):
        """
        Creates an empty graph
        """
        self.start = None
        self.end = None
        self.size = 0
        self.connections = {}
        self.adj = {}
        self.values = {}

    def _create_node(self, value):
        return self.Node(value)

    def switch(self, value):
        """ if node is closed this function will open it
        if node is open this function will close it
        :returns True
        """
        node = self.values[value]
        if node.open:
            node.open = False
        else:
            node.open = True
        return True

    def _link(self, node_1, node_2, weight=0):
        if self.size == 0 and node_1 != node_2:
            self.start = node_1
            self.size = 2
        elif node_1 == node_2:
            if self.size == 0:
                self.start = node_1
                self.end = node_1
            self.size = 1
        elif (not node_2.parents and not node_2.paths) or (not node_1.parents and not node_1.paths):
            self.size += 1
        link = (node_1, node_2)
        node_1.paths.append(node_2)
        node_2.parents.append(node_1)
        self.connections[(node_1.data, node_2.data)] = weight
        if node_1 != node_2:
            self.end = list(self.adj.keys())[-1]
        return link

    def link_two_nodes(self, value_1, value_2, weight=0):
        """
        creates a link from node corresponding to value_1 and node corresponding to value_2
        if graph has no links, first node will become start of graph
        the last added node will become the end of the graph.
        :param value_1: data of first node
        :param value_2: data of the destination node
        :param weight: weight of path
        :return: the link between node_1 and node_2
        """
        node_1 = None
        node_2 = None
        for key in self.adj.keys():
            if value_1 == key.data:
                node_1 = key
            if value_2 == key.data:
                node_2 = key
        if node_1 is None and node_2 is None and value_1 == value_2:
            node_1 = self._create_node(value_1)
            self.adj[node_1] = node_1.paths
            self.values[value_1] = node_1
            return self._link(node_1, node_1, weight)
        if node_1 is None:
            node_1 = self._create_node(value_1)
            self.adj[node_1] = node_1.paths
            self.values[value_1] = node_1
        if node_2 is None:
            node_2 = self._create_node(value_2)
            self.adj[node_2] = node_2.paths
            self.values[value_2] = node_2
        return self._link(node_1, node_2, weight)

    def _remove_link(self, node_1, node_2):
        node_1.paths.remove(node_2)
        self.connections.pop((node_1.data, node_2.data))

    def remove_node(self, value):
        """
        :param value: data of node
        :return: Removes node from graph and returns that same node and removes all connections to node
        """
        node = self.values[value]
        for parent in node.parents:
            self._remove_link(parent, node)
            if not parent.parents and not parent.paths:
                self.adj.pop(parent)
                self.size -= 1
        for path in node.paths:
            if (node.data, path.data) in self.connections.keys():
                self.connections.pop((node.data, path.data))
                path.parents.remove(node)
                if not path.parents and not path.paths:
                    self.adj.pop(path)
                    self.size -= 1

        node.parents.clear()
        node.paths.clear()
        self.adj.pop(node)
        self.size -= 1

    def clear_graph(self):
        """ Resets the graph
        """
        self.adj.clear()
        self.connections.clear()
        self.nodes_explored = 0
        self.size = 0
        self.start = None
        self.end = None

    def display_nodes(self):
        """
        :return: string with all paths of the graph, together with the weight of the path
        """
        links = []
        for key, value in self.connections.items():
            links.append("Path: " + str(key) + ", Weight: " + str(value))
        string = str(links)
        return string

    def number_of_paths(self):
        """
        :return: number of paths in graph
        """
        return 0 if not self.connections else len(self.connections)

    def size_of_graph(self):
        """
        :return: number of nodes in graph
        """
        return len(self.adj)

    def _dfs_search(self, node):
        visited_nodes = list()
        stack = deque()
        stack.append(node)
        while len(stack) > 0:
            node = stack.pop()
            if node.data not in visited_nodes:
                visited_nodes.append(node.data)
                for neighbor in node.paths:
                    if neighbor.open:
                        if neighbor.data not in visited_nodes:
                            stack.append(neighbor)
        return visited_nodes

    def _dfs_path(self, node, end):
        visited_nodes = list()
        q = deque()
        q.append([node.data])
        while len(q) > 0:
            path = q.pop()
            vertex = path[-1]
            vertex_node = self.values[vertex]
            if vertex_node == end:
                return path
            elif vertex not in visited_nodes:
                for neighbor in vertex_node.paths:
                    if neighbor.open:
                        new_path = list(path)
                        new_path.append(neighbor.data)
                        q.append(new_path)
                visited_nodes.append(vertex)

        return visited_nodes if end.data in visited_nodes else None

    def _bfs_search(self, node):
        visited_nodes = list()
        q = deque()
        q.append(node)
        while len(q) > 0:
            node = q.popleft()
            if node.data not in visited_nodes:
                visited_nodes.append(node.data)
                for neighbor in node.paths:
                    if neighbor.open:
                        if neighbor.data not in visited_nodes:
                            q.append(neighbor)
        return visited_nodes

    def _bfs_path(self, node, end):
        visited_nodes = list()
        q = deque()
        q.append([node.data])
        while len(q) > 0:
            path = q.popleft()
            vertex = path[-1]
            vertex_node = self.values[vertex]
            if vertex_node == end:
                return path
            elif vertex not in visited_nodes:
                for neighbor in vertex_node.paths:
                    if neighbor.open:
                        new_path = list(path)
                        new_path.append(neighbor.data)
                        q.append(new_path)
                visited_nodes.append(vertex)

        return visited_nodes if end.data in visited_nodes else None

    def bfs(self, start):
        """
        :param start: the data of node in which the bfs search will start
        :return: list of all the nodes in graph, in bfs order.
        """
        start_node = self.values[start]
        return self._bfs_search(start_node)

    def dfs(self, start):
        """
        Dfs-search the graph
        :param start: the data of node in which the dfs search will start
        :return: list of all the nodes in graph, in dfs order, dfs search is done with stack calls.
        """
        start_node = self.values[start]
        return self._dfs_search(start_node)

    def find_path(self, start, end, search='dfs'):
        """
        This method returns a list with nodes visited to get from the start node to the end node.
        Dfs-search path is set as default. If path is not found the method returns None.
        :param start: the data of node in which the path search will start.
        :param end: the data of node in which the path search will end.
        :param search: specifies what type of search will be used to find the path. 'dfs' and 'bfs' are alternatives.
        :return: list of nodes visited, giving the path from start to end node.
        """
        start_node = self.values[start]
        end_node = self.values[end]
        if search == 'dfs':
            return self._dfs_path(start_node, end_node)
        elif search == 'bfs':
            return self._bfs_path(start_node, end_node)
        else:
            return None
