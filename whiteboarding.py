# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

ex1 = ''
ex2= 'abcabcbb'
ex3= 'bbbbb'
ex3= 'pwwkew'

def longestSubstring(s):
    if not s:
        return 0
    # sliding window 0(n)
    # brute force (check everything) 0(n**2)
    left = 0
    right = 1
    seen = [s[left]]
    biggestString = 1
    while right < len(s):
        print(biggestString)
        print()
        while s[right] in seen:
            # before moving the left pointer, remove the it's value from the list
            seen.remove(s[left])
            # left moves
            left += 1
        seen.append(s[right])
        # updating what is currently the biggest
        if len(seen)>biggestString:
            biggestString = len(seen)
        right += 1
    return biggestString


