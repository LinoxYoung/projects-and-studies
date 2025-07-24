def checkPrimeFrequency(nums):
        def verf(c):
            l = []
            for i in range(2,c):
                if c%i == 0:
                    l.append("c")
            return "c" not in l
        l2 = []
        for i in range(2,len(nums)+1):
            if verf(i):
                l2.append(i) 
        l3 = []          
        for c in range(0,len(nums)):
            if nums.count(nums[c]) in l2:
              l3.append("x") 
        return "x" in l3  