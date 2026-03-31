class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {}
        indegree = {} # num prereqs for each course

        for course in range(numCourses):
            pre_map[course] = []
            indegree[course] = 0

        for course, prereq in prerequisites:
            pre_map[prereq].append(course)  # prereq → course
            indegree[course] += 1
        
        print(pre_map)
        print(indegree)
        
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        finish = 0
        while q:
            curr = q.popleft()
            finish += 1
            for nei in pre_map[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return finish == numCourses
