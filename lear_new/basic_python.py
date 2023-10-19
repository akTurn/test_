class Solution:
    def celToFnht(self,C):
        F = C*(9 / 5) + 32
        print("Celsius to Fahrenheit :" ,F)

    def areaRectangle(self,width,length):
        A = width * length
        print("Area of rectangle :",A)

    def greetings(self,name,age):
        print(f"Welcome {name} and you are {age} years old !!!")


    def evenOdd(self,num):
        if(num % 2 == 0):
            print(f"{num} is even number")
        else:
            print(f"{num} is odd number")


    def maxMin(self,list):
        print("Maximum value in the list :",max(list))
        print("Minimum value in the list :",min(list),end="")


    def palindrome(self,string):
        n = len(string)
        for i in range(n):
            if string[i] == string[n-1]:
              n -= 1
            else:
              return False
              break
        return True


    def compoundInterest(self,principal,interest,time):

        Amount = principal*(pow((1 + (interest / 100)),time))
        CI  = Amount - principal

        # positive x, positive y (x**y)
        print("Positive x and positive y : ", end="")
        print(pow(4, 3))

        print("Negative x and positive y : ", end="")
        # negative x, positive y (-x**y)
        print(pow(-4, 3))

        print("Positive x and negative y : ", end="")
        # positive x, negative y (x**-y)
        print(pow(4, -3))

        print("Negative x and negative y : ", end="")
        # negative x, negative y (-x**-y)
        print(pow(-4, -3))

        return CI


    def numberOfDays(self,Numberofdays:int):

        Numberofyears = round(Numberofdays / 365.25)
        Numberofmonths = round(Numberofdays / 30)
        Numberofweeks = Numberofmonths*4

        return Numberofyears,Numberofmonths,Numberofweeks

    def count_substrings(self,string):
        n = len(string)
        return (n * (n + 1)) // 2

    def printPalindromSubstrings(self,string):
        n = len(string)
        substrings = []
        palindrome_substring = []

        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = string[i:j]
                substrings.append(substring)
                n1 = len(substring)
                for i in range(n1):
                    if substring[i] == substring[n1 - 1]:
                        n1 -= 1
                        palindrome_substring.append(substring)

        return substrings,palindrome_substring

    def print_substrings(self,string):
        n = len(string)
        substrings = []
        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = string[i:j]
                substrings.append(substring)

        return substrings


    def containsDuplicate(self, nums:list[int]) -> bool:
       """ dup_nums = []
        for i in range(len(nums)):
            print(i,"i",nums)
            for j in range(i+1,len(nums)):
                print("j",nums[i],nums[j])
                if nums[i] != nums[j]:
                    print()
                    return False

        return True
        """

       def has_duplicates(nums):
           for i in range(len(nums)):
               for j in range(i + 1, len(nums)):
                   if nums[i] == nums[j]:
                       return True  # Found a duplicate
           return False  # No duplicates found


       nums = [1,3, 2, 4]
       if has_duplicates(nums):
           print("The list has duplicates")
       else:
           print("The list does not have duplicates")




    #def sumofPositiveInteger(self,list):

solution = Solution()

#c = float (input("Enter the celsius :"))
#result = solution.celToFnht(c)

#w = float(input("Enter the width :"))
#l = float(input("Enter the length :"))
#area = solution.areaRectangle(w,l)

"""

grt=solution.greetings('Nigel',45)

num=solution.evenOdd(38)

mxmn=solution.maxMin([12,67,45,89])

pldrm = solution.palindrome('abdbia')
print("is the string is Palindrome :",pldrm)

cmpound =solution.compoundInterest(10000, 10.25, 5)
print("Compound Interrst is :",cmpound)

years, months, weeks = solution.numberOfDays(780)
print(f" Number of years :{years} \n Number of months :{months} \n Number of weeks :{weeks} ")


main_string = "malayalam"
num_substrings =solution.count_substrings(main_string)
print(f"The number of substrings in '{main_string}' is {num_substrings}.")


main_string = "babab"
substrings =solution.print_substrings(main_string)

for substring in substrings:
    print(substring)


main_string = "babad"
substrings,pstrings =solution.printPalindromSubstrings(main_string)

#for substring in pstrings:
   # print(substring)
"""

nums = [1,2,4,3,3,4,3,2,4,2]
duplicate = solution.containsDuplicate(nums)
print(duplicate)

