class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')':'(', ']':'[', '}':'{'}
        checking = [] # stack

        for c in s:
            if c in pair.values(): # opening
                checking.append(c) # 入栈
            else: # closing, 检验checking顶上是否是匹配的opening
                if (not checking) or (checking.pop() != pair[c]):
                    return False
        
        return not checking # 检验opening是否全部出栈
        # O(n); O(n)