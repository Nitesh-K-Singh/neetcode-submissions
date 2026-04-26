class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # strategy 

        # 1. take one pass and store numbers, count in key value dict

        result = {}
        for i in nums:
            result[i] = result.get(i, 0) + 1
        

        # 2. sort the dict in descending order according to count(value)
        result_list = sorted(result.items(), key = lambda x: x[1], reverse = True) 

        # 3. return first k keys from sorted dict

        target = [i[0] for i in result_list][:k]
        return target
        