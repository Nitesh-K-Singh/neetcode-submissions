class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # method 1: sorted, two loops,

        n = len(strs)
        sorted_strs = [sorted(s) for s in strs]

        # return [sorted_strs[0] == sorted_strs[-1]]

        output = []
        hit = set()
        for i in range(n):
            if i not in hit:
                output.append([i])
                hit.add(i)
                for j in range(i + 1, n):
                    if sorted_strs[i] == sorted_strs[j]:
                        output[-1].append(j)
                        hit.add(j)

        return [[strs[i] for i in output[j]] for j in range(len(output))]
