class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            num1, num2 = num2, num1 # let num1 always short
        
        # 翻转num1, num2,之后的结果再翻转回来
        s1 = num1[::-1] # 77
        s2 = num2[::-1] # 654
        carry = 0 
        m,n = len(s1),len(s2)
        # 填充s1至s2的长度 [m,n)
        for _ in range(n-m):
            s1 += "0"

        res = [] # 先用一个list接收结果

        for i in range(n):
            # not convert the inputs to integers directly 但是没说可以转换字符
            cur_sum = int(s1[i])+int(s2[i])+carry #7+6=13
            carry, digit = divmod(cur_sum,10) # 1,3
            res.append(str(digit)) # ["3"]
        if carry:
            res.append(str(carry))
        return "".join(res[::-1])
        # O(n); O(n)
        
