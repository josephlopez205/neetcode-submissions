class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_s = {}
        chars_t = {}
        for char in s:
            if char not in chars_s:
                chars_s[char] = 1
            else:
                chars_s[char] += 1
        for char in t:
            if char not in chars_t:
                chars_t[char] = 1
            else:
                chars_t[char] += 1
        if len(chars_s) != len(chars_t):
            return False
        else:
            for key in chars_s:
                if key not in chars_t:
                    return False
                elif chars_s[key] != chars_t[key]:
                    return False
        return True
        