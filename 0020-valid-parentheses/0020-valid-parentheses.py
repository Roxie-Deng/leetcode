class Solution:
    def isValid(self, s: str) -> bool:
        # 配对处理
        def isPair(c1:str,c2:str) -> bool:
            pair = c1+c2
            if pair == "()" or pair == "[]" or pair == "{}":
                return True
            return False

        if len(s) == 0 or len(s) % 2 != 0:
            return False

        left = {'(','[','{'}
        right = {')',']','}'}
        # 利用stack后进先出的特性，遇到left就入栈，遇到right就left和right一起出栈,最后检查栈是否为空
        ans = []

        for i in range(len(s)):
            if s[i] in left:
                ans.append(s[i])
            if s[i] in right:
                if not ans or not isPair(ans[-1],s[i]):
                    return False
                ans.pop()
        return ans == []
        # O(n); O(n)