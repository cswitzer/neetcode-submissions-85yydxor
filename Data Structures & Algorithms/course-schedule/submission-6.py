class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Track how many prerequisites each course has (incoming edges)
        # Start with 0 for all courses
        indegree = {i: 0 for i in range(numCourses)}
        
        # Track which courses become available after completing each course
        # adj[pre] = list of courses that need 'pre' as a prerequisite
        adj = {i: [] for i in range(numCourses)}
        
        # Build the dependency graph from prerequisites
        # For each [course, pre] pair:
        for course, pre in prerequisites:
            # This course has one more prerequisite to satisfy
            indegree[course] += 1
            
            # When we complete 'pre', we can make progress toward 'course'
            adj[pre].append(course)
        
        # Find all courses we can start with (no prerequisites required)
        # These are our entry points into the course sequence
        q = deque()
        for course in indegree:
            if indegree[course] == 0:
                q.append(course)
        
        # Count how many courses we can successfully complete
        finish = 0
        
        # Process courses in valid order (topological sort)
        while q:
            # Take a course we can complete right now
            node = q.popleft()
            finish += 1
            
            # Check all courses that were waiting for this prerequisite
            for nei in adj[node]:
                # One less prerequisite blocking this course
                indegree[nei] -= 1
                
                # If all prerequisites are now satisfied, we can take this course
                if indegree[nei] == 0:
                    q.append(nei)
        
        # If we completed all courses, there's no cycle (valid schedule exists)
        # If we couldn't complete some courses, they're stuck in a cycle
        return finish == numCourses