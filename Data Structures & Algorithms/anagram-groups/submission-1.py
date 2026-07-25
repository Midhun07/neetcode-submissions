class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # first sort the string and then store in dict
        # increase the counter as you find the anagrams

        sorted_dict = {"".join(sorted(s)):[] for s in strs}

        for stri in strs:
            sorted_dict["".join(sorted(stri))].append(stri)
        
        return(list(sorted_dict.values()))
