class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        idxs = [i for i in range(len(timestamp))]
        idxs.sort(key=lambda i: timestamp[i])
        #idxs of tuples sorted in chronological order

        v = defaultdict(list)
        #organize by name
        #iterate in chronological order
        for ts_idx in idxs:
            v[username[ts_idx]].append(website[ts_idx])

        counts = defaultdict(int)
        
        q = []
        def rec(arr, start, k):
            nonlocal counts
            print(f"start: {start} k: {k} q: {q}")
            if len(q) == 3:
                merged = ' '.join(q)
                counts[merged] += 1
                #print(counts)
                return
            #recursively find and add all possible unique subarr of size k
            visited = set()
            print(f"i range: {start}, {len(arr) - k}")
            for i in range(start, len(arr) - k + 1):
                if arr[i] in visited:
                    continue
                visited.add(arr[i])
                q.append(arr[i])
                rec(arr, i + 1, k-1)
                q.pop()

        for name in list(v.keys()):
            print(f" updated counts state: {dict(counts)}")
            print(f"---------------------")
            print(f"{name}: {v[name]}")
            rec(v[name], 0, 3)
        
        print(dict(counts))
        max_count = max(counts.values())
        ties = [pattern for pattern in list(counts.keys()) if counts[pattern] == max_count]
        print(f"ties: {ties}")
        return min(ties).split()
        
                