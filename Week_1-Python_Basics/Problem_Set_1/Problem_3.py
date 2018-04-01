# Problem 3

# (15/15 points)
# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if
# s = 'azcbobobegghakl', then your program should print:
# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print:
# Longest substring in alphabetical order is: abc

# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we
# suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and
# cleared your head.


# Paste your code into this box
start = 0
end = 0
maxim = ""
while start < len(s)-1:
    while end < len(s):
        if end + 1< len(s) and ord(s[end+1]) >= ord(s[end]):
            end += 1
        else:
            if len(maxim) < len(s[start:end+1]):
                maxim = s[start:end+1]
            start = end + 1
            end += 1
            break

print(maxim)