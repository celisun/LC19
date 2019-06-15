class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) / 2
            if target == nums[r]: return r
            if target < nums[r]:
                if target <= nums[mid] <= nums[r]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[l] <= nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
        return l if nums[l] == target else -1

