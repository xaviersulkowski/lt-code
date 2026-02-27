class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        # approach 1 - join to string it's O(strs * i log i)
        # for i in strs: 
        #     groups["".join(sorted(i))].append(i)

        # return [v for v in groups.values()]

        # approach 2 - ord position count, it's O(s * strs) time 
        for s in strs: 
            # 26 char in alphabet 
            counts = [0] * 26
            for i in s: 
                counts[ord(i) - ord('a')] += 1 
            
            groups[tuple(counts)].append(s)
        
        return list(groups.values())
