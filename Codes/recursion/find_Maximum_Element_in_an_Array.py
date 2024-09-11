'''
Problem 5: Find Maximum Element in an Array
Input: [1, 5, 3, 9, 20]
Output: 9
'''
ip = [1, 5, 3, 9, 20]

def find_max_num(ip):
    if len(ip) == 1:
        return ip[0]
    if ip[1]>ip[0]:
        return find_max_num(ip[1:])
    else:
        ip[0], ip[1] = ip[1], ip[0]
        return find_max_num(ip[1:])

print(find_max_num(ip))