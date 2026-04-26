class Solution:
    def isPalindrome(self, s: str) -> bool:

        # approah: 
        # 1. delete all spaces somehow
        # 2: start with i in range(len(s)//2 + 1)
        # 3. Check is s[i] = s[-i] for all. return treu

        p = ''.join(c.lower() for c in s if c.isalnum())

        if len(p) <=1:
            return True
            
        for i in range(len(p)//2 + 1):
            if p[i] != p[-i-1]:
                return False
            
            
        return True

        