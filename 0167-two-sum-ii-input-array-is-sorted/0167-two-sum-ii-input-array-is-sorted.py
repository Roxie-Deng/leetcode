class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # make use of SORTED: two pointers
        left = 0
        right = len(numbers)-1

        while left<right:
            s = numbers[left] + numbers[right]
            if s == target:
                break
            if s < target:
                left += 1
            else:
                right -= 1

        return [left+1,right+1]
        
        # Time: O(n), Space: O(1)