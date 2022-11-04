
class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Graph:

    def __init__(self):
        self.al = {}

    def addNode(self, node, lst):
        self.al[node] = lst

    def dfs_visit(self, x, visited):
        if x in visited.keys():
            return
        else:
            print(x.name)
            visited[x] = True
            for w in self.al[x]:
                self.dfs_visit(w, visited)

    def dfs(self, node):
        print(node.name)
        visited = {node: True}
        for w in self.al[node]:
            self.dfs_visit(w, visited)


if __name__ == '__main__':
    

    A = Node('A', 1)
    B = Node('B', 2)
    C = Node('C', 3)
    D = Node('D', 4)
    E = Node('E', 5)

    g = Graph()
    g.addNode(A, [B])
    g.addNode(B, [C])
    g.addNode(C, [D])
    g.addNode(D, [E])
    g.addNode(E, [E])


    g.dfs(A)

#spyrogamiese
#me agapi panta
