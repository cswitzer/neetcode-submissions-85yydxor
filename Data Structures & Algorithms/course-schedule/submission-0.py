class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {course: [] for course in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        visiting = set()
        
        def dfs(course: int) -> bool:
            if course in visiting:
                return False
            if not pre_map[course]:
                return True
            
            visiting.add(course)
            for prereq in pre_map[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            # If course prereqs are all good, don't run through DFS again and waste time 
            pre_map[course] = []
            return True
        
        # Loop it since graphs may be disconnected e.g.
        # 1 -> 2
        # 3 -> 4
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True