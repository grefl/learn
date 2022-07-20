

def eventualSafeNodes(graph):
    seen = {}
    result = []
    def dfs(i):
        if i in seen:
            return seen[i]
        seen[i] = False
        for neighbour in graph[i]:
            if not dfs(neighbour):
                return seen[neighbour]
        seen[i] = True
        return True
    for i in range(len(graph)):
        if dfs(i):
            result.append(i)
    
    return result

        
