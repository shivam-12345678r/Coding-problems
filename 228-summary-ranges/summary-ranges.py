class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:return [] #Handling the edge case
        ans = []
        start = end  = str(nums[0]) #Initially we will keep the start and end pos and at same 
        for i in range(1 , len(nums)):
            if nums[i] != nums[i - 1] + 1:  #Checking if numbers are bounded 
                if start != end:     #If there exist a incrementing part
                    ans.append(start+'->'+end)
                else:
                    ans.append(start)
                start = end = str(nums[i])
            else:
                end = str(nums[i]) #Increasing the size of the existing bounds
        if start != end: #To handle the remaining elements out of the loop
            ans.append(start+'->'+end)
        else:
            ans.append(start)
        return ans