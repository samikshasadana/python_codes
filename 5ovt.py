class py_solution:    def twoSum(self, nums, target):        lookup = {}         for i, num in enumerate(nums):            if target - num in lookup:                return (lookup[target - num] + 1, i + 1)             lookup[num] = il=[]abc=py_solution()n=int(input())for i in range(n):    x=int(input())    l.append(x)x=int(input())print("index1=%d, index2=%d" % abc.twoSum(l,50))'''def test(numbers, target):    indexes = {}    for i,x in enumerate(numbers):        indexes[x] = indexes.get(x,[])+[i]    print (indexes)    for i,x in enumerate(numbers):        for j in indexes.get(target-x,[]):            if i < j:                print ("Found distinct components: ","at positions {3} and {4}".format(x, target-x, target, i, j))    print ("End.")test([1,4,5,7,9,6,2,1,5], 10)'''