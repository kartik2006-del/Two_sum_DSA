from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.qeue=deque()

    def ping(self, t):
        self.qeue.append(t)
        while self.qeue[0]<t-3000:
            self.qeue.popleft()
        return len(self.qeue)