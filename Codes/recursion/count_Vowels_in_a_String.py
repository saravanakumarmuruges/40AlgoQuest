'''
Problem 4: Count Vowels in a String
Input: "hello world"
Output: 3
'''
ip= "hello world"
def vowel_count(ip):
    if len(ip) ==0:
        return 0
    if ip[0] in ['a','e','i','o','u']:
        return 1+ vowel_count(ip[1:])
    else:
        return vowel_count(ip[1:])
print(vowel_count(ip))