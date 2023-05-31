from collections import deque

def makeGraph(arr, adj):
    for i in range(len(arr)):
        u, v = arr[i][0], arr[i][1]
        adj[u].append(v)
        adj[v].append(u)

def printGraph(adj):
    for i in range(len(adj)):
        print(i, end = "")
        for j in adj[i]:
            print(" -> ", j, end = "")
        print()

def DFS(adj, visited, curr):
    visited.add(curr)
    print(curr, end = " ")
    for i in adj[curr]:
        if i not in visited:
            DFS(adj, visited, i)

def BFS(adj, visited, curr):
    q = deque()
    visited.add(curr)
    q.append(curr)
    while q:
        curr = q.popleft()
        print(curr, end = " ")
        for i in adj[curr]:
            if i not in visited:
                visited.add(i)
                q.append(i)

v = int(input("Enter No.  of vertices : "))
e = int(input("Enter No. of edges : "))
arr = []
for i in range(e):
    print("Enter edge pair " + str(i+1) + " : ")
    arr.append(list(map(int, input().split())))
adj = [[] for i in range(v)]
makeGraph(arr, adj)
printGraph(adj)
print("DFS", end = " ")
visited = set()
for i in range(v):
    if i not in visited:
        DFS(adj, visited, i)
visited.clear()
print()
print("BFS", end = " ")
for i in range(v):
    if i not in visited:
        BFS(adj, visited, i)
