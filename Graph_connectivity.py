from DFS_BFS import bfs, read_graph

n,k, matrix = read_graph("in.txt")

if len(bfs(n, k, matrix)) == n:
    print("The graph is connected")
else:
    print("The graph is not connected")