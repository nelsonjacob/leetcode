'''
problem statement:

Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.

'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
    	

    	'''
    	idea: we must check every element of the str, without any additional memory

  		way to check the last element of the string and compare to the first element of the string


  		wasitacaroracatisaw


    	'''

    	start_el = 0
    	end_el = len(s) - 1


    	while start_el < end_el:
    		# check 1: s[start_el] is a alphanumeric char
    		if (!s[start_el].isAlpha()):
    			start_el += 1
    			continue
    		if (!s[end_el].isAlpha()):
    			end_el -= 1
    			continue


    		if lower([start_el]) != lower(s[end_el]):
    			return False
    			start_el += 1
    			end_el -= 1

    	return True




