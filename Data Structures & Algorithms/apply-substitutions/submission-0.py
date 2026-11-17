class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        """
        string contains placeholders formatted as 
        %{var}%

        replacements mapping 
        {var}: replacement value
            replacement value may contain placeholders too 

        Approach:
        perform DFS and replace/update the keys once a replacement value is detected
            - mark as visited (visited = a string with no placeholders/updated to hold no placeholders)
            so that resolving only happens once per key not every time it shows up in the text
        """
        no_placeholders = set()
        replacements = {var: replacement for var, replacement in replacements}
        replacements[text] = text

        def replace(var):
            raw = replacements[var]
            l = 0 
            res = []
            while l < len(raw):
                if raw[l] != "%":
                    res.append(raw[l])
                    l += 1
                else:
                    r = l + 1
                    while r < len(raw): 
                        if raw[r] == "%":
                            if raw[l + 1:r] not in no_placeholders:
                                replace(raw[l + 1:r])
                            res.append(replacements[raw[l + 1:r]])
                            l = r + 1
                            break
                        r += 1
                replacements[var] = "".join(res)
                no_placeholders.add(var)
                
        replace(text)
        return replacements[text]
