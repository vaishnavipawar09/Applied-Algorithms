def usingdfs(currnode, graph_network, visitednode):
    visitednode.add(currnode)  # to mark that curr node has been visited
    for neighbor in graph_network[currnode]:  # call all the nodes
        if neighbor not in visitednode:  # if not visited visit them
            usingdfs(neighbor, graph_network, visitednode)


def makeTunnels(n, tunnels):
    # dictionary is used that represents graph
    graph = {i: [] for i in range(n)}
    for ai, bi in tunnels:  # making it bi directional tunnel
        graph[ai].append(bi)
        graph[bi].append(ai)

    visited = set()
    components = 0  # count the number of connected components
    for ctr in range(n):
        if ctr not in visited:
            usingdfs(ctr, graph, visited)
            components += 1

    moreTunnels = components - 1  # for finding minimum tunnels we need

    if len(tunnels) < n - 1:  # if the condition of minimum tunnels is not satisfied
        return -1

    return moreTunnels


# Test cases
print(makeTunnels(4, [[0, 1], [0, 2], [1, 2]]))  # Expected output: 1
print(makeTunnels(6, [[0, 1], [0, 2], [0, 3], [1, 2]]))  # Expected output: -1
