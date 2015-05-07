class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if(len(s) != len(t)):
            return False
        dictionaryForS = {}
        dictionaryForT = {}
        for i in range(len(s)):
            if (dictionaryForS.get(s[i]) == dictionaryForT.get(t[i])):
                dictionaryForS.update({s[i]:i})
                dictionaryForT.update({t[i]:i})
            else:
                return False
        return True
