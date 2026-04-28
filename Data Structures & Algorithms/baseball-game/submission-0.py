class Solution:
    def calPoints(self, operations: List[str]) -> int:

        result = []
        ops = operations
        
        for i in range(len(ops)):
            if ops[i].isdigit():
                result.append(int(ops[i]))
            elif ops[i] == "+":
                result.append(result[-1] + result[-2])  # edge case out of index
            elif ops[i] == "D":
                result.append(2*result[-1])
            elif ops[i] == "C":
                result.pop(-1)
       
            
        
        

        return sum([int(x) for x in result])
                
        