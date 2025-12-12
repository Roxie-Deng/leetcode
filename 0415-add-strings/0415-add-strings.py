class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        ans = []
        carry = 0
        i = 0

        while i<len(num1) or i<len(num2) or carry: # 有任意一位数没处理完或者存在进位
            digit1 = int(num1[i]) if i<len(num1) else 0
            digit2 = int(num2[i]) if i<len(num2) else 0

            carry, digit = divmod(digit1+digit2+carry,10)

            ans.append(str(digit))

            i += 1
        
        return "".join(ans[::-1])

        # O(n); O(1)