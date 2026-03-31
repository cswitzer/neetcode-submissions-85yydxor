class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0 for _ in range(numCourses)]
        pre_map = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            indegree[course] += 1 # this course has n prereqs
            pre_map[pre].append(course) # complete pre before you can access the courses
        
        # initially load courses without prerequisites
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        order = []
        while q:
            prereq = q.popleft()
            order.append(prereq)
            # we completed this prereq, now we can subtract the prereq count by 1
            # for all courses this was a prereq for
            for course in pre_map[prereq]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)
        
        return order if len(order) == numCourses else []
