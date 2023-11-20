from collections import defaultdict

def DFS(graph: defaultdict(list), start: int, visited=None) -> None:
 """
    Perform Depth-First Search (DFS) on a graph starting from a given node.
    Parameters:
    - graph: defaultdict(list)
        An adjacency list representing the graph, where keys are nodes and values are lists of neighboring nodes.
    - start: int
        The starting node for DFS traversal.
    - visited: set, optional
        A set to keep track of visited nodes. Defaults to None, and is initialized as an empty set within the function.

    Algorithm:
    - If visited is not provided, create an empty set and name it visited
    - Mark the start node as visited
    - Print the value of the start node
    - for each neighbor in graph[start]:
        + if neighbor is not visited:
            ++ Recursively call DFS(graph, neighbor, visited)

    """

    

def BFS(graph: defaultdict(list), start: int) -> None:
    """
        Perform Breadth-First Search (BFS) on a graph starting from a given node.
        Parameters:
        - graph: defaultdict(list)
            An edge adjacency list representing the graph, where keys are nodes and values are lists of neighboring nodes.
        - start: int
            The starting node for BFS traversal.
        Algorithm:
        - Initialize an empty set called visited
        - Initialize an empty queue called queue
        - Enqueue the start node into the queue
        - Add the start node to the visited set
        - while the queue is not empty:
            + Dequeue a node from the front of the queue (current node)
            + Print the value of current
            + for each neighbor in graph[current]:
                ++ check if neighbor is not in visited:
                        +++ Enqueue neighbor into the queue
                        +++ Add neighbor to the visited set 

    """
    
T = int(input()) #number of test cases
while T:
    n = int(input()) #number of edges
    edge_list = []
    for _ in range(n):
        x, y = int(input().split())
        edge_list.append([x, y])
    graph = defaultdict(list) #edge adjacency list
    for edge in edge_list:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    start = int(input()) #node start
    print("DFS: ")
    DFS(graph, start)
    print()
    print("BFS: ")
    BFS(graph, start)
    print()
    T -= 1



