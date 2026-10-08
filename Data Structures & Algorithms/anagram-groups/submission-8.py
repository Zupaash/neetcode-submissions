class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create a dict
            # keys = tuples of letters, values = list of words matching the key when turned into a tuple

        # iterate through dictionary and add to a larger list + return

        by_group = {}

        for word in strs:
            ordered = tuple(sorted(word))
            
            if ordered in by_group:
                by_group[ordered].append(word)
            else:
                by_group[ordered] = [word]
                
        total_list = []

        for pair in by_group.values():
            total_list.append(pair)

        return total_list