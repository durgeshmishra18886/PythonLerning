from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_num={}

        for i in range(len(nums)):
            current_num=nums[i]
            required = target - nums[i]
            if required in seen_num:
                original_index=seen_num[required]
                return [original_index,i]
            seen_num[required]=i
        return []



