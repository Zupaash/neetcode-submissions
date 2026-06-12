class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        list_s = []
        list_t = []

        # store characters in s first

        for i in range(0, len(s)):
            list_s.append(s[i])

        # store characters in t next

        for j in range(0, len(t)):
            list_t.append(t[j])

        # sort lists

        list_s.sort()
        list_t.sort()

        return list_s == list_t
