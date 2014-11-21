class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    result = []
    def subsetsWithDup(self, S):
        self.result = [[]]
        S.sort()
        for i in range(len(S)):
            self.helper([S[i]], i, S)
        return self.result

    def helper(self, array, index, S):
        if(len(array) < 1):
            return 
        if( self.result.count(array) != 1  ):
            self.result.append(array)
        for i in range(index+1,len(S)):
            if( self.result.count(array + [S[i]]) != 1  ):
                self.result.append(array + [S[i]])
                self.helper(array + [S[i]], i, S)
                
            

