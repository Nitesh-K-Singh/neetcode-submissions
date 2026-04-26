class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force
        # check every subsequence.. so starting at i, 
        # compplexity: O(n^2), O(1)


        n = len(s)
        if n<= 1:
            return n

        l = 0
        for i in range(n):
            l_temp = 1
            # d_temp ={}
            d_temp[s[i]] = 1
            for j in range(i+1,n):
                if s[j] in d_temp.keys():
                    break
                else:
                    d_temp[s[j]] = 1
                    l_temp = l_temp + 1 
            
            l = max(l, l_temp)

        return l
                

        