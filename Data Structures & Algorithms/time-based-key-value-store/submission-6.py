class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Order of timestamps is already guaranteed, so manual checking here is not necessary
        Key only consists of values between 1 <= key <= 1000
        """
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        """Should use binary search to find the value of they key at the timestamp"""
        if not key in self.timemap:
            return ""
        
        timestamps = self.timemap[key]
        low, high = 0, len(timestamps) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if timestamps[mid][1] == timestamp:
                return timestamps[mid][0]
            elif timestamps[mid][1] < timestamp:
                low = mid + 1
            else:
                high = mid - 1
        
        # When the timestamp arg is higher than the max, high is the latest timestamp
        # When the timestamp arg is lower than the min, high is -1 which equates to ""
        # In any case, high always keeps track of what it believes to be the max element
        return timestamps[high][0] if high >= 0 else ""

