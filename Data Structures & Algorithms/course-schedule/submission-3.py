class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        [[1, 0], [2, 1], [3, 1]] where n = 4
        0 prereq for 1
        1 prereq for 2
        1 prereq for 3

        prereqs = {
            0: [],
            1: [0],
            2: [1],
            3: [1]
        }

        0 -> 1 -> 2
             |
             3

        numCourses = 2, prerequisites = [[0,1],[1,0]]
        0 -> 1
        ^    |
        ------

        Not possible since 0 is a prereq of 1 and 1 is a prereq of 0
        """

        prereqs = { course: [] for course in range(numCourses) }
        for course, pre in prerequisites:
            prereqs[course].append(pre)
        visiting = set()

        def dfs(course: int) -> bool:
            if course in visiting:
                return False
            if not prereqs[course]:
                return True
            
            visiting.add(course)
            for pre in prereqs[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


