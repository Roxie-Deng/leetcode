class Solution:
    def isValid(self, s: str) -> bool:
        search_dict = {")":"(","]":"[","}":"{"}
        opening = []

        for char in s:
            if char in search_dict.values(): # opening
                opening.append(char)
            elif char in search_dict: # closing
                if not opening or search_dict[char] != opening[-1]:
                    return False
                opening.pop()
        
        return not opening

        # O(n);O(n)