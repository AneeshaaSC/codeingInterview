class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        if( A == None ):
            return None
        if(len(A) < 1):
            return 0
        
        tempDict = {}
        result = []
        for i in A:
            if ( not tempDict.has_key(i) ):
                result.append(i)
                tempDict.update({i:0})
            else:
                if (tempDict.get(i) == 0):
                    tempDict.update({i:1})
                    result.remove(i)
        return result[0]
