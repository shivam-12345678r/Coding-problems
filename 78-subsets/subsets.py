class Solution(object):
    def subsets(self, nums):
        def back(start,path):
            res.append(path[:])

            for i in range(start,len(nums)):
                path.append(nums[i])

                back(i + 1,path)
                path.pop()

        res = []
        back(0,[])
        return res
                
        

       
        