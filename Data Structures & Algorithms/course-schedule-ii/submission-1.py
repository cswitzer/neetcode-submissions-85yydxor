class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0 for _ in range(numCourses)]
        adj = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            indegree[course] += 1
            # we cannot access the course without completing pre
            adj[pre].append(course)
        
        q = deque()
        # starting from leaf nodes, or nodes with no prereqs
        for course, degree in enumerate(indegree):
            if degree == 0:
                q.append(course)
        
        order = []
        while q:
            # prereq completed, update indegrees to reflect that
            # e.g. 5: [6, 7], if I complete 5 then indegrees for 6, 7 must go down by 1
            complete = q.popleft()
            order.append(complete)
            for course in adj[complete]:
                indegree[course] -= 1
                # We completed all the prereqs for this course. Add it for processing
                if indegree[course] == 0:
                    q.append(course)
        
        return order if len(order) == numCourses else []
