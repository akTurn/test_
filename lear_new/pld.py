def printPalindromSubstrings(string):
    n = len(string)
    substrings = []
    #palindrome_substring = []
    longest_palindrome = ""

    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = string[i:j]
            substrings.append(substring)
            n1 = len(substring)
            is_palindrome = True  # Assume it's a palindrome unless proven otherwise

            for k in range(n1 // 2):
                if substring[k] != substring[n1 - k - 1]:
                    is_palindrome = False
                    break

            #if is_palindrome:
                #palindrome_substring.append(substring)

            if is_palindrome and n1 > len(longest_palindrome):
                longest_palindrome = substring



    return substrings, longest_palindrome

substrings, palindrome_substrings = printPalindromSubstrings("rijtetvjirij")

#print("All Substrings:", substrings)
print("Palindrome Substrings:", palindrome_substrings)
