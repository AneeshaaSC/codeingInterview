class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        dictionary = {}
        for index,value in enumerate(strs):
            temp = value
            value = map(str,value)
            value.sort()
            value = ''.join(value)
            if(dictionary.get(value) == None):
                dictionary.update({value:[temp]})
            else:
                test = dictionary.get(value)
                test.append(temp)
                dictionary.update({value:test})
        a = []
        for i in dictionary.values():
            if (len(i) > 1):
                a += i
        if (len(a) >= 1):
            return a
        else:
            return []

