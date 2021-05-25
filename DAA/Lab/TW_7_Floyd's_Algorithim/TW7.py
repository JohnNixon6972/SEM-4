# Implement All-Pairs Shortest Paths Problem using Floyd's algorithm.

infinity = 999


def solve(graph, vertices):
    distance = list(map(lambda i: list(map(lambda j: j, i)), graph))

    for m in range(vertices):
        for n in range(vertices):
            for o in range(vertices):
                distance[n][o] = min(
                    distance[n][o], distance[n][m]+distance[m][o])

    DisplaySoln(distance, vertices)


def DisplaySoln(distance, vertices):
    for i in range(vertices):
        for j in range(vertices):
            if distance[i][j] == infinity:
                distance[i][j] = "inf"

    for rows in distance:
        print(rows)


def main():
    vertices = int(input("Enter the number of vertices :: "))
    graph = [[infinity for _ in range(vertices)] for _ in range(vertices)]
    edges = int(input("Enter the number of edges :: "))
   
    for i in range(edges):
        x, y, w = map(int, input(f"Enter the vertices of edges {i+1} with its weight :: ").split())
        graph[x-1][y-1] = w
        print(graph)

    solve(graph, vertices)


if __name__ == "__main__":
    main()
