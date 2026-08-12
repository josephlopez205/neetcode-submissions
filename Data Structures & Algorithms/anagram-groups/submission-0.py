class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        common_dictionary = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string not in common_dictionary:
                common_dictionary[sorted_string] = []
            common_dictionary[sorted_string].append(string)
        return list(common_dictionary.values())
