# https://leetcode.com/problems/valid-palindrome/   

def isPalindrome(s): 
    
    # two pointers approach
    l, r = 0, len(s) - 1
    while l < r:
        # if character at the left pointer is not alphanumeric, move the left pointer to the right
        if not s[l].isalnum():
            l += 1
        # if character at the right pointer is not alphanumeric, move the right pointer to the left
        elif not s[r].isalnum():
            r -= 1
        # now that the characters are alphanumeric but not the same, s is not a palindrome
        elif s[l].lower() != s[r].lower():
            return False
        # we a potential palindrome
        else:
            l += 1
            r -= 1
    return True

s1 = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = " "
print(isPalindrome(s1), isPalindrome(s2), isPalindrome(s3))