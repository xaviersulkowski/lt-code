class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # m is a pointer at latest real num 1 
        # n is a pointer at latest num 2 

        # m_ insert pointer
        m_ = m + n 

        while m > 0 and n > 0: 
            if nums1[m - 1] < nums2[n - 1]: 
                nums1[m_ - 1] = nums2[n - 1]
                n -= 1 
            else: 
                nums1[m_ - 1] = nums1[m - 1]
                m -= 1
            m_ -= 1

        while n > 0:
            nums1[m_ -1] = nums2[n - 1]
            n -= 1
            m_ -= 1

