def read_graph(file_name):
    with open(file_name, "r") as f:
        n, k = map(int, f.readline().split())
        matrix = []

        for i in range(n):
            row = list(map(int, f.readline().split()))
            matrix.append(row)

    return n, k, matrix


def bfs(n, k, matrix):
    visited = []
    order = []
    queue = []

    queue.append(k)
    visited.append(k)
    while queue:
        node = queue.pop(0)
        order.append(node)

        for i in range(n):
            if matrix[node - 1][i] == 1 and i + 1 not in visited:
                queue.append(i + 1)
                visited.append(i + 1)
    return order


def dfs(n, k, matrix):
    visited = []
    order = []
    stack = []

    stack.append(k)
    visited.append(k)

    while stack:
        node = stack.pop()
        order.append(node)

        for i in range(n - 1, -1, -1):
            if matrix[node - 1][i] == 1 and i + 1 not in visited:
                stack.append(i + 1)
                visited.append(i + 1)

    return order


n, k, matrix = read_graph("in.txt")

print("-".join(map(str, bfs(n, k, matrix))))
print("-".join(map(str, dfs(n, k, matrix))))
