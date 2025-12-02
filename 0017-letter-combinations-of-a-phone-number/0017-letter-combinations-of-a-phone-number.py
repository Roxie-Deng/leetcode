class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # find all paths: backtracing (recursive)
        # current problem: iterate through letters mapped to the current digit (digits[i]); append each one to "path" (possible str)
        # next problem: move to the next digit; append letters of it
        # Arg progress: i+1
        if not digits:
            return []
        
        # a seq to store digit-letter mappings; tuple, able to access by idx
        MAPPINGS = "","","abc","def","ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
        ans = []
        path = [""]*len(digits) # fixed len

        def dfs(i):
            if i == len(digits): # curren path is already created
                ans.append("".join(path))
                return
            for c in MAPPINGS[int(digits[i])]:
                path[i] = c # cover it directly
                dfs(i+1)
        
        dfs(0)
        return ans