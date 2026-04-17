class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count_s = {}
        for i in s:
            count_s[i] = count_s.get(i,0) + 1

        count_t = {}
        for i in t:
            count_t[i] = count_t.get(i,0) + 1

        return count_t == count_s


        




   # method 1, just sort and check for equality     
        # return ''.join(sorted(s)) == ''.join(sorted(t)) 
            # -- returns strings

        # return sorted(s) == sorted(t) # returns list

    # method 2, use dictionary to keep counts: 

        