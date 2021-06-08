# From a given vertex in a weighted connected graph, find shortest paths to other vertices
# using Dijkstra's algorithm.

infinity = 9999


def shortest_dist(vertices, shortest_paths, Path_Set):

    shortest = infinity

    for vertex in range(vertices):
        if shortest_paths[vertex] < shortest and Path_Set[vertex] == False:
            shortest = shortest_paths[vertex]

            shortest_path_index = vertex

    return shortest_path_index


def Dijkstra(vertices, graph, source_vertex):

    shortest_paths = [infinity] * vertices
    shortest_paths[source_vertex] = 0

    Path_Set = [False] * vertices

    for i in range(vertices):

        dist_index = shortest_dist(vertices, shortest_paths, Path_Set)

        Path_Set[i] = True

        for vertex in range(vertices):
            if graph[dist_index][vertex] > 0 and Path_Set[vertex] == False and shortest_paths[vertex] > shortest_paths[dist_index] + graph[dist_index][vertex]:
                shortest_paths[vertex] = shortest_paths[dist_index] + \
                    graph[dist_index][vertex]

    print()
    print("Vertex \tDistance from Source")
    for node in range(vertices):
        print(node, "\t", shortest_paths[node])
    print()


def printGraph(graph):
    print()

    print("Given Graph in Matrix Form :: ")
    for rows in graph:
        print(*rows, sep="\t")

    print()


def main():
    vertices = int(input("Enter the number of vertices :: "))
    graph = [[infinity for _ in range(vertices)] for _ in range(vertices)]
    ch = 1

    while ch == 1:
        x, y, w = map(int, input(
            "Enter the vertices of a edge with its weight :: ").split())
        graph[x-1][y-1] = w

        ch = int(
            input("Press 1 to enter one more edge values or any other key to compute :: "))
        print()

    printGraph(graph)
    Dijkstra(vertices, graph, 0)


if __name__ == "__main__":
    main()
