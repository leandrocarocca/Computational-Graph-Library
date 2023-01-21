from graphlib import Graph

g = Graph()

g.link_two_nodes("Stockholm", "Paris", 2000)
g.link_two_nodes("Paris", "Tokyo")
g.link_two_nodes("Tokyo", "Stockholm")
g.link_two_nodes("Tokyo", "Barcelona")
g.link_two_nodes("Barcelona", "Madrid")
g.link_two_nodes("Stockholm", "Madrid")
g.link_two_nodes("Stockholm", "Tokyo")

print(g.display_nodes())
print("DFS-SEARCH: ", g.dfs("Stockholm"))
print("BFS-SEARCH: ", g.bfs("Stockholm"))
print("DFS-PATH: ", g.find_path("Stockholm", "Madrid"))
print("BFS-PATH: ", g.find_path("Stockholm", "Madrid", 'bfs'))
print(g.connections)

