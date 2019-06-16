class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = nums1, nums2
        m, n = len(A), len(B)
        if m > n:
            m, n, A, B = n, m, B, A

        l, r = 0, m
        target = (m + n + 1) / 2
        while l <= r:
            i = (l + r) / 2
            j = target - i

            if i > 0 and A[i - 1] > B[j]:
                r = i - 1
            elif i < m and B[j - 1] > A[i]:
                l = i + 1
            else:
                m1 = max(A[i - 1] if i > 0 else float('-inf'), B[j - 1] if j > 0 else float('-inf'))
                if (m + n) % 2: return m1
                m2 = min(A[i] if i < m else float('inf'), B[j] if j < n else float('inf'))
                # print m1, m2
                return (m1 + m2) / 2.0
        return -1
