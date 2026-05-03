class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) - 2*int(len(s)/2) == 1:
            return False
        
        # traverse from left to right, keep adding opening and closing 
        
        # dict mapping
        mapping = {')': '(', '}': '{', ']': '['}
        mapping_keys = list(mapping.keys())
        track = []
        for bracket in s:
            if bracket in mapping_keys:
                if track[-1] == mapping.get(bracket):
                    track.pop()
                else:
                    return False
            
            else:
                track.append(bracket)
        
        # return mapping_keys
        # return track

        return len(track) == 0


     

        