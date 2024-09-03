from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        idx1 = 0
        idx2 = 0
        array = []
        if m == 0 and n == 0:
            return array
        if m == 0:
            for idx in range(n):
                nums1[idx] = nums2[idx]
            return nums1
        if n == 0:
            return nums1
        for idx in range(m+n):
            if m <= idx1:
                nums1[idx] = nums2[idx2]
                idx1+=1
                idx2+=1
            elif nums1[idx1] > nums2[idx2]:
                temp = nums2[idx2]
                nums2[idx2] = nums1[idx1]
                nums1[idx1] = temp
                nums2.sort()
                idx1 += 1
            else:
                idx1+=1
        return nums1

sol = Solution()
# print("array: ", sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
# print("array: ", sol.merge([4,5,6,0,0,0], 3, [1,2,3], 3))
# [-1,0,0,3,3,3,0,0,0]
# 6
# [1,2,2]
# 3
print("array: ", sol.merge([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3))