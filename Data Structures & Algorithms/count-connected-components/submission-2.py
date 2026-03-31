class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = {i: i for i in range(n)} # init every node parent of self
        rank = [1 for _ in range(n)]

        def find(n1: int):
            res = n1

            # loop until we find a node who is its own parent
            while res != parent[res]:
                parent[res] = parent[parent[res]] # set parent of res to grandparent for compression optimization
                res = parent[res]

            return res
        
        def union(n1: int, n2: int):
            par1, par2 = find(n1), find(n2)

            # if both n1's and n2's parents are the same
            # there is no reason to perform a union
            if par1 == par2:
                return 0
            
            if rank[par2] > rank[par1]:
                parent[par1] = par2
                rank[par2] += rank[par1]
            else:
                parent[par2] = par1
                rank[par1] += rank[par2]
            return 1
            
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        
        return res