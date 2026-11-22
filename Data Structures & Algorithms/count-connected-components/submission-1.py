class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for i in edges:
            adjList[i[0]].append(i[1])
            adjList[i[1]].append(i[0])
        count = 0
        visited = set()
        def dfs(mylist):
            for x in mylist:
                if x not in visited:
                    visited.add(x)
                    dfs(adjList[x])

        for i in adjList.keys():
            if i not in visited:
                visited.add(i)
                count += 1
                dfs(adjList[i])
        return count + n - len(visited)