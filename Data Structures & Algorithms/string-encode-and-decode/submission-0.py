class Solution:

    def encode(self, strs: List[str]) -> str:
        string = []
        for s in strs:
            # append length of the string
            string.append(str(len(s)))
            # append #
            string.append("#")
            # append string
            string.append(s)
            # append #
        return "".join(string)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            word = s[j + 1 : j + 1 + length]
            res.append(word)

            i = j + 1 + length
        return res
                
