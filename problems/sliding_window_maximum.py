class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums: return []
        if k >= len(nums): return [max(nums)]
        res, stack = [], []
        for i, a in enumerate(nums):
            if stack and stack[0] + k == i:
                stack.pop(0)
            while stack and nums[stack[-1]] < a:
                stack.pop()
            stack.append(i)
            if i >= k-1: res.append(nums[stack[0]])
        return res