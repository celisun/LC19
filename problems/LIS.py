class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 2 8 9 10 4 5 5 5 5 1 6 5 
        # binary search solution
        if not nums: return 0
        
        res = 0
        tail = [nums[0]] * len(nums)
        for n in nums: 
            i, j = 0, res
            while i < j: 
                mid = (i + j) / 2
                if tail[mid] < n: 
                    i = mid + 1
                else: 
                    j = mid 
            # print i, j, tail
            tail[i] = n 
            res = max(res, i+1)
        return res 
        
        
            
# bisect approach nlogn    
#         from bisect import * 
#         sub = []
#         for n in nums: 
#             idx = bisect_left(sub, n)
#             if idx == len(sub): 
#                 sub.append(n)
#             else: 
#                 sub[idx] = n               
#         return len(sub)
        
