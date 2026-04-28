class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        count = {0: students.count(0), 1: students.count(1)}
        for s in sandwiches:
            if count[s] > 0:
                count[s] -= 1
            else:
                return sum(count.values())
        return 0

        # n = len(studentys) # also equal to number of sandwiches
        # for i in range(n):
        
        # while comdition :

    
        #     if students[0] = sandwhiches[0]:
        #         students.remove(0)
        #         sandwhiches.remove(0)
        #     else:
        #         temp = students[0]
        #         studnets[0] = students[1] # need a shifting operation
        #         students[n-1] = studnets[temp]
        