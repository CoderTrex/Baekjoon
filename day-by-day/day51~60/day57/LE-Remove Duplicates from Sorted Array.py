from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 1
        for i in range(1, len(nums)): 
            if nums[cnt] in nums[:cnt]: 
                del nums[cnt] 
                cnt -=1
            cnt += 1
        return len(nums)

sol = Solution()
nums = [1,1,2]
print(sol.removeDuplicates(nums)) # 2
print(nums) # [1, 2]