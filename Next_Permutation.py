ass Solution:
    # @param num, a list of integer
    # @return nothing (void), do not return anything, modify num in-place instead.
    def nextPermutation(self, num):
        sortedNum = sorted(num)[::-1]
        if(num == sortedNum):
            num.reverse()
            return 
        for i in range(len(num)):
            tempNum = num[i+1::]
            top = num[i]
            sortedNum = sorted(tempNum)[::-1]
            if(tempNum == sortedNum):
                temp=top
                for x in sortedNum[::-1]:
                    if(x > temp):
                        top = x
                        break
                if(top == temp):
                    continue
                tempNum.append(temp)
                tempNum.remove(top)
                tempNum.sort()
                del(num[i::])
                num.extend(tempNum)
                num.insert(i,top)
                return 
