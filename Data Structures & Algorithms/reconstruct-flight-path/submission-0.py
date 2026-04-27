class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        # satisfies lexical order requirement when multiple solutions exist
        tickets.sort()
        for src, dest in tickets:
            adj[src].append(dest)
        
        result = ["JFK"]
        def dfs(src):
            if len(result) == len(tickets) + 1:
                return True
            
            # This means we cannot get anywhere from this node (no edges)
            if src not in adj:
                return False
            
            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                result.append(v)
                if dfs(v):
                    return True
                adj[src].insert(i, v)
                result.pop()
            return False
        
        dfs("JFK")
        return result
