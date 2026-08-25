class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        computing each label is O(n) (longest string size, adding each char = O(n), list to string -> O(1) (string length is 26, constant)
        compute label m times
        
        store m strings of len 26 => O(m) memory 
        """
        offset = ord('a')
        def group_label(s):
            #index as list then stringify for return val
            nonlocal offset
            res = [0] * 26
            for ch in s:
                res[ord(ch) - offset] += 1
            return str(res)

        groups = defaultdict(list)
        for s in strs:
            groups[group_label(s)].append(s)

        return list(groups.values())
