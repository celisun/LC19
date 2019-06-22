from heapq import *
class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l, self.r = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heappush(self.l, -heappushpop(self.r, num))
        if len(self.r) < len(self.l):
            tmp = heappop(self.l)
            heappush(self.r, -tmp)

    def findMedian(self):
        """
        :rtype: float
        """
        if not self.r: return -1

        if len(self.r) == len(self.l):
            return (self.r[0] + -self.l[0]) / 2.
        else:
            return self.r[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()