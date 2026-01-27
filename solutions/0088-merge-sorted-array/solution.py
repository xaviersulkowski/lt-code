class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # nums1 = [1,1,2,3,0,0,0], m = 4, nums2 = [2,5,6], n = 3
        # nums1[0] = 1 and nums2[0] = 2 should I add it? no, because nums1[1] = 1, move nums1 pointer 
        # nums1[1] = 1 and nums2[0] = 2 should I add it? yes, because nums1[2] = 2, add and move nums1 and nums2 pointer 
        # but I cannot add elements without moving the whole array
        # BUT I know that at the end I have the free space, so let's do it in the reverse order 
        # we need 3 pointers, one on real end of nums1, end of nums2 and end of nums1 
        # nums1[3] = 3 and nums2[2] = 6, I can replace nums1[6] with greater value 


        ptr1 = m - 1 
        ptr2 = n - 1
        last = len(nums1) - 1 

        while ptr1 >= 0 and ptr2 >= 0: 
            print(f"ptr1={ptr1}:{nums1[ptr1]}, ptr2={ptr2}:{nums2[ptr2]}, nums={nums1}")
            if nums2[ptr2] > nums1[ptr1]: 
                nums1[last] = nums2[ptr2]
                ptr2 -= 1 
            else:
                nums1[last] = nums1[ptr1]
                ptr1 -= 1 
            last -= 1
        
        print(f"ptr1={ptr1}, ptr2={ptr2}, nums={nums1}")
            
        while ptr2 >= 0: 
            nums1[last] = nums2[ptr2]
            ptr2 -= 1
            last -= 1
        
