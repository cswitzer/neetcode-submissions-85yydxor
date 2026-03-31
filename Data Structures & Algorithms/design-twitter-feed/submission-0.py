class Twitter:
    """
    loop through tweets, where each tweet at the front of the queue is the most recent
    (earliest timestamp)
    """

    def __init__(self):
        self.count = 0 
        self.users = defaultdict(set) # user (int): followees (set[int]) 
        self.tweets = defaultdict(list) # user (int): tweets (list[tuple[count, tweetId]])

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        self.users[userId].add(userId)
        for followee_id in self.users[userId]:
            if followee_id in self.tweets:
                index = len(self.tweets[followee_id]) - 1
                count, tweet_id = self.tweets[followee_id][index]
                # the count will always be unique
                # the tweet_id is what is returned in result
                # the combination of the followee_id and index - 1 tells us which tweet to add next
                # from the user that is being followed
                heapq.heappush(min_heap, [count, tweet_id, followee_id, index - 1])
        
        while min_heap and len(res) < 10:
            count, tweet_id, followee_id, index = heapq.heappop(min_heap)
            res.append(tweet_id)
            if index >= 0:
                # the next tweet by that same user
                count, tweet_id = self.tweets[followee_id][index]
                heapq.heappush(min_heap, [count, tweet_id, followee_id, index - 1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
