class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 固定大小的窗口，在s上滑动
        np = len(p) 
        ns = len(s)
        ans = []
        cnt_p = Counter(p)

        '''
        for i in range(ns-np+1):
            if cnt_p == Counter(s[i:i+np]):
                ans.append(i)
        return ans
        # for循环*计数器 O(ns*np)
        # O(26)
        '''

        # 继续优化: cnt_s不需要每次都重新数
        cnt_s = Counter()

        for right,c in enumerate(s):
            cnt_s[c] += 1

            left = right+1-np
            if left<0:
                continue
            
            if cnt_s == cnt_p:
                ans.append(left)
            
            cnt_s[s[left]] -= 1
        return ans

        # O(n)
        # O(26)