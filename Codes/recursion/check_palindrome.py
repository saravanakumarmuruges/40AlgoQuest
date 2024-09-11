'''Problem Statement: 
Write a recursive function to check if a given string is a palindrome. 
A palindrome is a word, number, or phrase that reads the same backward as forward.
Input: "madam"
Output: True
'''
st = 'madam'

def palindrome(st):
    if len(st) <= 1:
        return True
    if st[0] == st[-1]:
        return palindrome(st[1:-1])
    else:
        return False

print(palindrome('madam'))