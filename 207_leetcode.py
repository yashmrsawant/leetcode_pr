"""
https://leetcode.com/problems/course-schedule/description/
"""

"""
given adjacency matrix;
travel from a start node in all possible ways

"""
import pdb 
# code to convert input to adjacency matrix
A = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0], [1, 0, 0, 0]]


def pre_checks(A):
    Ns = []
    for i in range(len(A)):
        Ns.append(len(A[i]))
    for i in range(len(Ns)):
        assert len(A) == Ns[i]
    
    V = []
    for i in range(len(A)):
        v = []
        for j in range(len(A[i])):
            if A[i][j] != 0:
                v.append(j)
        V.append(v)
    return len(A), V


# The function pre_checks(A) is called with A as argument, and its return value is assigned to N.
# It's assumed that this function performs some preliminary checks and returns the number of nodes.
N, Vo = pre_checks(A)

# A 2D list named edgeVisitFlag is created with N rows and N columns, all initialized with 0.
# This list is used to keep track of the edges that have been visited in the graph.

# Print the number of nodes
print("Number of nodes %d"%(N))

# An empty list named paths is created to store all the paths in the graph.
paths = []
print(Vo)


# a for loop is used to iterate over all the nodes in the graph.
for node_i in range(N):

    _, V = pre_checks(A)
    edgeVisitFlag = []
    for k in range(N):
        e = []
        for m in range(N):
            e.append(0)
        edgeVisitFlag.append(e)
    
    # edgeVisitFlag = [[0] * N] * N

    # a stack is created to keep track of the nodes in the current path.
    stack = []
    # A list named visitedNodeFlags is created to keep track of the nodes that have been visited.
    visitedNodeFlags = [0] * N

    # The current node is added to the stack and marked as visited.
    stack.append(node_i)
    visitedNodeFlags[node_i] = 1
    if node_i == 0:
        pdb.set_trace()
    # pdb.set_trace()
    # A while loop is used to continue the process as long as there are nodes in the stack.
    while len(stack) != 0:
        print(stack)
        addFlag = 0
        # The node at the top of the stack is considered as the current node.
        currentNode = stack[-1]

        # The list of edges for the current node is retrieved from A.
        a_m1 = A[currentNode]

        # A for loop is used to iterate over all the nodes connected to the current node.
        countNodes = 0
        for node_j in V[currentNode]:
            # print(edgeVisitFlag)
            if node_j != currentNode:
                if edgeVisitFlag[currentNode][node_j] == 0 and visitedNodeFlags[node_j] == 0 and a_m1[node_j] != 0:
                    stack.append(node_j)
                    V[currentNode].remove(node_j)
                    visitedNodeFlags[node_j] = 1
                    edgeVisitFlag[currentNode][node_j] = 1
                    addFlag = 1
                    break
        if addFlag == 1:
            continue
        for node_j in V[currentNode]:
            if node_j != currentNode:
                if edgeVisitFlag[currentNode][node_j] == 0 and visitedNodeFlags[node_j] == 1 and a_m1[node_j] != 0:
                    countNodes = countNodes + 1

        if countNodes == len(Vo[currentNode]):
            stack.append("END")
        # a new path is created and all the nodes in the stack are added to it.
        if stack[-1] == "END":
            stack.pop()

            path = []
            for node_k in stack:
                path.append(node_k)

            # The path is added to the list of paths.
            paths.append(path)

        # The current node is removed from the stack.
        visitedNodeFlags[stack.pop()] = 0



for path in paths:
    print(path)






