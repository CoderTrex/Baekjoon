from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        copy_s = s.copy()
        len_s = len(copy_s)
        for i in range(len_s):
            s[i] = copy_s[len_s - 1 - i]
        