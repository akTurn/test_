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

    def isValid(self, s: str) -> bool:
        stack = []
        chrsTostart = ['(', '{', '[']
        chrsToend = [')', '}', ']']

        for char in s:
            if char in chrsTostart:
                stack.append(char)
            elif char in chrsToend:
                if not stack:
                    return False  # Unmatched closing parenthesis

                top = stack.pop()

                if (char == ')' and top != '(') or \
                   (char == '}' and top != '{') or \
                   (char == ']' and top != '['):
                    return False  # Mismatched opening and closing parenthesis

        return len(stack) == 0  # True if all parentheses are balanced

    def lenLongestSubstring(self, string: str):
        max_length = 0
        substring = []

        for char in string:

            if char in substring:
                print(substring,max_length)
                while substring and substring[0] != char:

                    substring.pop(0)
                if substring:

                    substring.pop(0)
            substring.append(char)
            max_length = max(max_length, len(substring))

        return max_length

    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        substrings = []
        longest_palindrome = ""

        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = s[i:j]
                substrings.append(substring)
                n1 = len(substring)
                is_palindrome = True  # Assume it's a palindrome unless proven otherwise

                for k in range(n1 // 2):
                    if substring[k] != substring[n1 - k - 1]:
                        is_palindrome = False
                        break

                if is_palindrome and n1 > len(longest_palindrome):
                    longest_palindrome = substring

        return longest_palindrome



solution = Solution()
result_bool = solution.isValid('()[(())]')
print("is valid ? :",result_bool)

ip = [2,7,11,15,78,34,56,67,23,13,79,80,90]
tg = 36
res_add=solution.sum_list(ip,tg)
print(f"Two index values whose sum is equal to  {tg} are :",res_add)

rest_unique = solution.lenLongestSubstring('ederfetgey')
print("Length of the longest substring without repeating characters:", rest_unique)

long_palindrome =solution.longestPalindrome('malayalam')
print("The longest palindrome is :",long_palindrome)