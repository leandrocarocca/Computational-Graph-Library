import unittest
from graphlib import Graph


class TestGraphLib(unittest.TestCase):
    def setUp(self):
        self.g = Graph()

    def tearDown(self):
        self.g.clear_graph()

    def graph_1(self):
        """
        7 8 9
        4 5 6
        1 2 3
        """
        self.g.link_two_nodes(1, 2)
        self.g.link_two_nodes(1, 4)
        self.g.link_two_nodes(2, 1)
        self.g.link_two_nodes(2, 3)
        self.g.link_two_nodes(2, 5)
        self.g.link_two_nodes(3, 2)
        self.g.link_two_nodes(3, 6)
        self.g.link_two_nodes(4, 1)
        self.g.link_two_nodes(4, 5)
        self.g.link_two_nodes(4, 7)
        self.g.link_two_nodes(5, 2)
        self.g.link_two_nodes(5, 4)
        self.g.link_two_nodes(5, 6)
        self.g.link_two_nodes(5, 8)
        self.g.link_two_nodes(6, 3)
        self.g.link_two_nodes(6, 5)
        self.g.link_two_nodes(6, 9)
        self.g.link_two_nodes(7, 4)
        self.g.link_two_nodes(7, 8)
        self.g.link_two_nodes(8, 5)
        self.g.link_two_nodes(8, 7)
        self.g.link_two_nodes(8, 9)
        self.g.link_two_nodes(9, 6)
        self.g.link_two_nodes(9, 8)

    def test_graph(self):
        self.assertIsNone(self.g.start, True)
        self.assertIsNone(self.g.end, True)
        self.assertEqual(self.g.size, 0)
        self.assertEqual(self.g.connections, {})
        self.assertEqual(self.g.adj, {})

    def test_remove_node(self):
        self.g.link_two_nodes("Paris", "Stockholm", 1000)
        self.g.link_two_nodes("Tokyo", "Stockholm", 2000)
        self.assertEqual(self.g.size, 3)
        self.g.remove_node("Stockholm")
        self.assertEqual(self.g.size, 0)
        self.assertEqual(self.g.connections, {})

    def test_clear_graph(self):
        self.g.link_two_nodes("Paris", "Stockholm", 1000)
        self.g.link_two_nodes("Tokyo", "Stockholm", 2000)
        self.g.clear_graph()
        self.assertIsNone(self.g.start, True)
        self.assertIsNone(self.g.end, True)
        self.assertEqual(self.g.size, 0)
        self.assertEqual(self.g.connections, {})
        self.assertEqual(self.g.adj, {})

    def test_display_node(self):
        self.g.link_two_nodes("Stockholm", "Paris", 1000)
        self.g.link_two_nodes("Paris", "Tokyo", 2000)
        self.g.link_two_nodes("Tokyo", "Stockholm", 3000)
        string = str(["Path: ('Stockholm', 'Paris'), Weight: 1000",
                      "Path: ('Paris', 'Tokyo'), Weight: 2000",
                      "Path: ('Tokyo', 'Stockholm'), Weight: 3000"])
        self.assertEqual(self.g.display_nodes(), string)

    def test_find_link(self):
        self.assertEqual(self.g.display_nodes(), "[]")
        self.g.link_two_nodes("Stockholm", "Paris", 1000)
        self.g.link_two_nodes("Paris", "Tokyo", 2000)
        self.g.link_two_nodes("Tokyo", "Stockholm", 3000)

    def test_number_of_paths(self):
        self.assertEqual(self.g.number_of_paths(), 0)
        self.g.link_two_nodes("Stockholm", "Paris", 1000)
        self.g.link_two_nodes("Paris", "Tokyo", 2000)
        self.g.link_two_nodes("Tokyo", "Stockholm", 3000)
        self.assertEqual(self.g.number_of_paths(), 3)
        self.g.remove_node("Stockholm")
        self.assertEqual(self.g.number_of_paths(), 1)
        self.g.clear_graph()
        self.assertEqual(self.g.number_of_paths(), 0)

    def test_size_of_graph(self):
        self.assertEqual(self.g.size_of_graph(), 0)
        self.g.link_two_nodes("Stockholm", "Paris", 1000)
        self.g.link_two_nodes("Paris", "Tokyo", 2000)
        self.assertEqual(self.g.size_of_graph(), 3)
        self.g.remove_node("Stockholm")
        self.assertEqual(self.g.size_of_graph(), 2)
        self.g.remove_node("Paris")
        self.assertEqual(self.g.size_of_graph(), 0)

    def test_dfs(self):
        self.graph_1()
        self.assertEqual(self.g.dfs(5), [5, 8, 9, 6, 3, 2, 1, 4, 7])
        self.assertEqual(self.g.dfs(1), [1, 4, 7, 8, 9, 6, 5, 2, 3])

    def test_bfs(self):
        self.graph_1()
        self.assertEqual(self.g.bfs(1), [1, 2, 4, 3, 5, 7, 6, 8, 9])
        self.assertEqual(self.g.bfs(5), [5, 2, 4, 6, 8, 1, 3, 7, 9])

    def test_find_path(self):
        self.graph_1()
        self.assertEqual(self.g.find_path(1, 9), [1, 4, 7, 8, 9])
        self.assertEqual(self.g.find_path(1, 9, 'bfs'), [1, 2, 3, 6, 9])
        self.g.switch(6)
        self.g.switch(7)
        self.assertEqual(self.g.find_path(1, 9), [1, 4, 5, 8, 9])
        self.assertEqual(self.g.find_path(1, 9, 'bfs'), [1, 2, 5, 8, 9])
        self.g.switch(6)
        self.g.switch(7)
        self.assertEqual(self.g.find_path(1, 6), [1, 4, 7, 8, 9, 6])
        self.assertEqual(self.g.find_path(1, 6, 'bfs'), [1, 2, 3, 6])


if __name__ == '__main__':
    unittest.main()
