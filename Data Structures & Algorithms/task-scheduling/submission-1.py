class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        create a priority max queue where the tasks with the most entries in the array will
        be prioritized.
        Create a regular queue as well to have tasks wait in line when cooling down.
        Tasks on the queue will cooldown for n seconds before being added back to the priority
        max queue to be processed
        If no tasks are on the priority queue, we will stand idle
        When the priority queue and queue are both empty, we return the minimum number of cycles
        """
        counts = Counter(tasks)
        
        pq = [-c for c in counts.values()]
        heapq.heapify(pq)

        cooldown = deque() # [ready_time, remaining_count]
        time = 0

        while pq or cooldown:
            time += 1

            # execute a task if available
            if pq:
                # max heaps store in negatives, so adding 1 subtracts it
                count = 1 + heapq.heappop(pq)
                if count:
                    cooldown.append((time + n, count))
            
            # move task back to heap if cooldown finished
            if cooldown and cooldown[0][0] == time:
                ready_time, count = cooldown.popleft()
                heapq.heappush(pq, count)
        
        return time

