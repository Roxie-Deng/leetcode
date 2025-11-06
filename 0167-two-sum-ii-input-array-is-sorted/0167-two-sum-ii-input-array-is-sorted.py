class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        showed = {} # key: num, val: idx
        
        # cuurent num_c + num_p in {showed nums} = target
        # add num_c in {showed nums}
        for idx, num in enumerate(numbers):
            if (target-num) in showed:
                return [showed[target-num]+1,idx+1]
            
            showed[num] = idx

        