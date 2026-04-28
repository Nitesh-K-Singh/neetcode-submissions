class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        n = len(arr)
        max_arr = [0]*n
        current = arr[-1]
        max_arr[-1] = -1
        for i in range(n-2,-1,-1):
            current = max(current, arr[i+1])
            max_arr[i] = current

        return max_arr

        