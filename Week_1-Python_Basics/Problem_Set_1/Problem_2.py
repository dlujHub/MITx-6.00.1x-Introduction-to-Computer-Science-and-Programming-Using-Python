# Problem 2
# (10/10 points)
# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your
# program should print
# Number of times bob occurs is: 2

string = "bob"
i = 0
count=0
while i<=len(s)-2:
    if s[i:i+3] == string:
        count += 1
    i +=1
print(count)