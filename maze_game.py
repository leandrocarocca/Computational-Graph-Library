from graphlib import Graph
from random import getrandbits

graph = Graph()


def graph_1():

    """
    7 8 9
    4 5 6
    1 2 3
    """
    graph.link_two_nodes(1, 2)
    graph.link_two_nodes(1, 4)
    graph.link_two_nodes(2, 1)
    graph.link_two_nodes(2, 3)
    graph.link_two_nodes(2, 5)
    graph.link_two_nodes(3, 2)
    graph.link_two_nodes(3, 6)
    graph.link_two_nodes(4, 1)
    graph.link_two_nodes(4, 5)
    graph.link_two_nodes(4, 7)
    graph.link_two_nodes(5, 2)
    graph.link_two_nodes(5, 4)
    graph.link_two_nodes(5, 6)
    graph.link_two_nodes(5, 8)
    graph.link_two_nodes(6, 3)
    graph.link_two_nodes(6, 5)
    graph.link_two_nodes(6, 9)
    graph.link_two_nodes(7, 4)
    graph.link_two_nodes(7, 8)
    graph.link_two_nodes(8, 5)
    graph.link_two_nodes(8, 7)
    graph.link_two_nodes(8, 9)
    graph.link_two_nodes(9, 6)
    graph.link_two_nodes(9, 8)
    print("7 8 9")
    print("4 5 6")
    print("1 2 3")

def graph_2():
    graph.link_two_nodes(1, 1, 1000)
    graph.link_two_nodes(1, 2, 2000)
    graph.link_two_nodes(1, 5, 3000)
    graph.link_two_nodes(2, 1, 4000)
    graph.link_two_nodes(2, 3, 5000)
    graph.link_two_nodes(2, 5, 6000)
    graph.link_two_nodes(3, 2, 7000)
    graph.link_two_nodes(3, 4, 8000)
    graph.link_two_nodes(4, 3, 9000)
    graph.link_two_nodes(4, 5, 1000)
    graph.link_two_nodes(4, 6, 11000)
    graph.link_two_nodes(5, 1, 2)
    graph.link_two_nodes(5, 2, 123)
    graph.link_two_nodes(5, 4, 55)
    graph.link_two_nodes(6, 4, 10000)


def create_maze():
    maze = []
    for i in graph.adj.keys():
        random_bit = getrandbits(1)
        random_boolean = bool(random_bit)
        if random_boolean:
            graph.switch(i.data)
        else:
            maze.append(i.data)
    return maze


graph_1()
print(graph.find_path(1, 6))
print(graph.find_path(1, 6, 'bfs'))
