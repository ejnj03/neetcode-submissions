class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        chars = set("".join(words))
        adj = {char : [] for char in list(chars)}

        word_lens = [len(word) for word in words]
        max_len = max(word_lens)

        def get_groups(group, psn):
            if len(group) <= 1:
                return []
            #get groups of words with same word at psn
            word_groups = {}
            prev_char = None
            
            for word_idx in range(len(group)):
                word = group[word_idx]
                print(psn, word)
                if len(word) - 1 < psn: 
                    if group[0] != word:
                        return None
                    continue
                char = word[psn]
                if not prev_char:
                    prev_char = char
                    word_groups[prev_char] = []
                if char != prev_char:
                    
                    #add adj prev char -> curr char
                    adj[prev_char].append(char)
                    #if this char was already seen its invalid
                    if char in word_groups:
                        return None
                    #create its word group
                    word_groups[char] = [word]
                    #update prev char
                    prev_char = char
                else:
                    word_groups[prev_char].append(word)
            return list(word_groups.values())
    

        curr_groups = [words]
        curr_pos = 0

        while True:
            if len(curr_groups) == 0:
                print("breaking")
                break
            new_groups = []
            for group in curr_groups:
                sub_groups = get_groups(group, curr_pos)
                print(adj, sub_groups)
                if sub_groups == None: return ""
                if len(sub_groups) == 0: continue
                new_groups.extend(sub_groups)
            curr_groups = new_groups
            curr_pos += 1

        print("adj", adj)

        res = []
        visited = set()
        def sort(char, prev):
            if char in visited: return True
            #if not visited but in prev means that contains cycle
            if char in prev: return False
            prev.add(char)  
            for nb in adj[char]:
                val = sort(nb, prev)
                if not val: return False
            visited.add(char)
            res.append(char)
            return True
        
        char_list = list(chars)
        for char in char_list:
            val = sort(char, set())
            if not val: return ""
        
        res.reverse()
        return "".join(res)
            





                
            
            
        