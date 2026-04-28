class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        
        return sorted(points, key = lambda p: p[0]**2 + p[1]**2)[:k]




        # # brute force:
        # # find and store all distnaces

        # distances = []
        # for point in points:
        #     distance = point[0]* point[0] + point[1]* point[1] 
        #     distances.append(distance)
        #      # take distance square, monotonic ordering
        # # sort distances in increasing order, while prserving index

        # result_dic = dict(enumerate(distances)) 
        # result_dic = sorted(result_dic.items(), key = lambda x: x[1])
    
        # return [points[i] for i, _ in result_dic[:k]]



        