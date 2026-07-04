class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s # O(n)
        if len(t)>len(s):
            return "" # O(1)
        
        cnt_t = Counter(t) # O(n)
        cnt_s = Counter() # 不用defaultdict(int)是因为后续的比较，避免隐式插入0键
        need = len(cnt_t) # 需要的不同字母的种类数
        formed = 0 # 已经匹配成功的种类数

        ans_left, ans_right = -1, len(s)

        left=0

        for right,ch in enumerate(s):
            cnt_s[ch] += 1
            if cnt_s[ch] == cnt_t[ch]:
                formed += 1
            
            while formed == need: # 窗口合法
                # 更新答案
                if right-left+1<ans_right-ans_left+1:
                    ans_left,ans_right=left,right
                #尝试收缩左边界
                left_ch = s[left]
                cnt_s[left_ch] -= 1
                if cnt_s[left_ch]<cnt_t[left_ch]:
                    formed -= 1
                left += 1
        return s[ans_left:ans_right+1] if ans_left != -1 else ""
        # O(n)
        # O(26)