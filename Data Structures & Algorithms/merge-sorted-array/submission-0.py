class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1 = 0
        idx2 = 0
        index = 0
        n1 = nums1.copy()
        n2 = nums2.copy()
        while idx1 < m and idx2 < n:
            if n1[idx1] <= n2[idx2]:
                nums1[index] = n1[idx1]
                idx1 += 1
                index += 1
            else:
                nums1[index] = n2[idx2]
                idx2 += 1
                index += 1
        while idx1 < m:
            nums1[index] = n1[idx1]
            index += 1
            idx1 += 1
        while idx2 < n:
            nums1[index] = n2[idx2]
            index += 1
            idx2 += 1
