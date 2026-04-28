class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums = nums1[:m]
        result = []

        i, j = 0, 0

        while i < m and j < n:
            if nums[i] <= nums2[j]:
                result.append(nums[i])
                i = i + 1

            else:
                result.append(nums2[j])
                j = j + 1


        if i < m:
            result = result + nums[i:]
        if j < n:
            result = result + nums2[j:]

        
        nums1[:] = result
        return result


       
        
        


        



        

        