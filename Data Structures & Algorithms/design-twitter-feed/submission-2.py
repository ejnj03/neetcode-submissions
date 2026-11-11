class Tweet:
    def __init__(self, tweetId, userId, tweetCount):
        self.tweetId = tweetId
        self.author = userId
        self.posted = tweetCount


class User:
    def __init__(self, userId):
        self.userId = userId
        self.followers = set()
        self.followees = set()
        self.tweets = deque()

    def post(self, tweet) -> None:
        self.tweets.appendleft(tweet)  # larger time = more recent

    def recieveFollow(self, follower) -> None:
        self.followers.add(follower)

    def recieveUnfollow(self, follower: int) -> None:
        if follower in self.followers:
            self.followers.remove(follower)

    def follow(self, followee: int) -> None:
        self.followees.add(followee)

    def unfollow(self, followee: int) -> None:
        if followee in self.followees:
            self.followees.remove(followee)


class Twitter:
    def __init__(self):
        self.users = {}  # userId : User object mapping
        self.count = 0 #current number of posts

    def getUser(self, userId):
        if userId not in self.users:
            self.users[userId] = User(userId)
        return self.users[userId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        user = self.getUser(userId)
        tweet = Tweet(tweetId, userId, self.count)
        user.post(tweet)
        self.count += 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        user = self.getUser(userId)
        followees = list(user.followees)
        followees.append(user)
        feed = []
        for followee in followees:
            # if the next most recent tweet of followee is less than the least recent tweet in the heap- can stop
            for tweet in list(followee.tweets):  # ordered most recent -> least recent
                if len(feed) >= 10 and tweet.posted < feed[0][0]:
                    break  # done with this followee
                heapq.heappush(feed, (tweet.posted, tweet.tweetId))
                while len(feed) > 10:
                    heapq.heappop(feed)

        return [tweet[1] for tweet in sorted(feed, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        follower = self.getUser(followerId)
        followee = self.getUser(followeeId)
        follower.follow(followee)
        followee.recieveFollow(follower)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        follower = self.getUser(followerId)
        followee = self.getUser(followeeId)
        follower.unfollow(followee)
        followee.recieveUnfollow(follower)
