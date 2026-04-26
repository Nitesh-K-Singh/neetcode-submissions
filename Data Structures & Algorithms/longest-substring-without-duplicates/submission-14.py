class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # sliding window
        # for any i in s find longest subsequence ending at i
        # 
        n = len(s)
        if n<= 1:
            return n

        d_temp = {}
        d_temp[s[0]] = 1
        left = 0
        global_count = 1
        local_count = 1
        for i in range(left+1,n):

            
            if s[i] in d_temp.keys():
                left = left + 1
                global_count = max(local_count, global_count)
                # local_count = local_count - 1
                # need to eject s[i] from d_temp
                
            else:
                local_count = local_count + 1
                d_temp[s[i]] = 1 
            
            global_count = max(local_count, global_count)
            

        return global_count


        # brute force
        # check every subsequence.. so starting at i, 
        # compplexity: O(n^2), O(1)
        
        # n = len(s)
        # if n<= 1:
        #     return n

        # l = 0
        # for i in range(n):
        #     d_temp ={}
        #     d_temp[s[i]] = 1
        #     l_temp = 1
        #     for j in range(i+1,n):
        #         if s[j] in d_temp.keys():
        #             break
        #         else:
        #             d_temp[s[j]] = 1
        #             l_temp = l_temp + 1 
            
        #     l = max(l, l_temp)

        # return l
                

        