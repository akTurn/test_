"""class Solution:
    def lenLongestSubstring(self,string:str)-> int:
        print("string",string)
        count = 0
        for i in range(len(string)):
            count= count + 1
            print(string[i],count)
            for j in string[i+1:]:
                count += 1
                print(j,count)
                if string[i] == j:
                 count -= 1
                 print("end",j,"count",count)
                 break


solution = Solution()
result = solution.lenLongestSubstring('arsdasd')


def lenLongestSubstring(string):
    max_length = 0
    substring = []

    for char in string:
        print(char)
        if char in substring:
            print(substring,max_length)
            while substring and substring[0] != char:
                print("test",substring[0])
                substring.pop(0)
            if substring:
                print("test1", substring)
                substring.pop(0)
        substring.append(char)
        max_length = max(max_length, len(substring))

    return max_length

result = lenLongestSubstring('ederfetgey')
print("Length of the longest substring without repeating characters:", result)

"""
class Solution:
    def uniqueLongestSubstring(self, string: str) -> int:
        max_length = 0  # Initialize the maximum length to 0

        for i in range(len(string)):
            char_set = set()  # Use a set to keep track of unique characters in the current substring
            print(i)
            for j in range(i, len(string)):
                print(char_set,max_length,j)
                if string[j] in char_set:
                    break  # If we find a repeating character, break out of the inner loop
                char_set.add(string[j])  # Add the character to the set
                max_length = max(max_length, len(char_set))

        return max_length  # Return the maximum length found

solution = Solution()
result = solution.uniqueLongestSubstring('arrsddas')
print("Length of the longest substring without repeating characters:", result)

