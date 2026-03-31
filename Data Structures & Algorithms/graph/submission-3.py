class Graph:
    
    def __init__(self):
        self.adj_list = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src] = set()
        if dst not in self.adj_list:
            self.adj_list[dst] = set()
        self.adj_list[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list[src]:
            return False
        self.adj_list[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list:
            return False

        if src == dst:
            return True

        visited = set()
        visited.add(src)

        def dfs(curr: int):
            visited.add(curr)
            for neighbor in self.adj_list.get(curr, []):
                if neighbor == dst:
                    return True
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False
        
        return dfs(src)
