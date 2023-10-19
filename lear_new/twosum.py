"""
Method 1 ---using index()

"""
"""

class Solution:
    def twoSum(self, nums, target):
          for i in nums:
            num1=i
            p1=nums.index(i)
            for j in nums[p1+1:]:
                num3=num1+j
                p2=nums.index(j)
                if num3==target:
                    output= [p1,p2]
          return output
ip = [2,7,11,15]
tg = 26
obj=Solution()
res=obj.twoSum(ip,tg)
print(res)

"""
"""
METHOD :2   using enumerate()
"""
class Solution:
    def sum_list(self,input,target):
        list_indices = {}
        result = []
        for index,list in enumerate(input):
            lookup = target-list

            print("items",lookup,list,list_indices)
            if lookup in list_indices:
                result=[list_indices[lookup],index]  #It's set to find pairs of numbers that sum to the target, but it returns the last pair of indices it encounters during the loop
                #break    ----Adding the break statement will make the code stop
                             # -----after finding the first pair of indices that sum to the target
                #result.append([list_indices[lookup],index]) #-----To find all pairs of indices that sum to the target

            list_indices[list] = index
        return result

ip = [2,7,11,15,78,34,56,67,23,13,79,80,90]
#ip=[3,3]
tg = 36
obj=Solution()
res=obj.sum_list(ip,tg)
print(res)