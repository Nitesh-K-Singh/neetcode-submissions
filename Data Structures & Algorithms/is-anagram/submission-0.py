class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

   # method 1, just sort and check for equality     
        return ''.join(sorted(s)) == ''.join(sorted(t))

    # method 2, use dictionary to keep counts: 