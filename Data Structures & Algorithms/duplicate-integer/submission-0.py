class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_hashmap = {}

        for i in nums:
            if i in my_hashmap:
                return True
            else:
                my_hashmap[i] = True
        
        return False