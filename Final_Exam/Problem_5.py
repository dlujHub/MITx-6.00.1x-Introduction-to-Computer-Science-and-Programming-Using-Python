# Problem 5
# 20.0/20.0 points (graded)
#
# Assume you are given two dictionaries d1 and d2, each with integer keys and integer values. You are also given a function f, that takes in two integers, performs an unknown operation on them, and returns a value.
#
# Write a function called dict_interdiff that takes in two dictionaries (d1 and d2). The function will return a tuple of two dictionaries: a dictionary of the intersect of d1 and d2 and a dictionary of the difference of d1 and d2, calculated as follows:
#
# intersect: The keys to the intersect dictionary are keys that are common in both d1 and d2. To get the values of the intersect dictionary, look at the common keys in d1 and d2 and apply the function f to these keys' values -- the value of the common key in d1 is the first parameter to the function and the value of the common key in d2 is the second parameter to the function. Do not implement f inside your dict_interdiff code -- assume it is defined outside.
# difference: a key-value pair in the difference dictionary is (a) every key-value pair in d1 whose key appears only in d1 and not in d2 and (b) every key-value pair in d2 whose key appears only in d2 and not in d1.
#
# Here are two examples:
#
# If f(a, b) returns a + b
# d1 = {1:30, 2:20, 3:30, 5:80}
# d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
# then dict_interdiff(d1, d2) returns ({1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90})
# If f(a, b) returns a > b
# d1 = {1:30, 2:20, 3:30}
# d2 = {1:40, 2:50, 3:60}
# then dict_interdiff(d1, d2) returns ({1: False, 2: False, 3: False}, {})
#
# def dict_interdiff(d1, d2):
#     '''
#     d1, d2: dicts whose keys and values are integers
#     Returns a tuple of dictionaries according to the instructions above
#     '''
#     # Your code here
#
# Paste your entire function, including the definition, in the box below. The function f will be automatically added to your code, do not paste it in the box. Do not leave any debugging print statements. Note that we ask you to write a function only -- you cannot rely on any variables defined outside your function for your code to work correctly.


def dict_interdiff(d1, d2):
    """
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    """
    def ff(a,b):
        return a + b
    def f(a,b):
        return a > b
    result = ({}, {})
    for key_a, value_a in d1.items():
        if key_a in d2.keys():
            result[0].setdefault(key_a, f(value_a, d2.get(key_a)))
            d2.pop(key_a)
        else:
            if type(f(key_a, value_a)) == int:
                result[1].setdefault(key_a, value_a)

    for key, value in d2.items():
        if type(f(key, value)) == int:
            result[1].setdefault(key, value)

    inter = {}
    diff = {}

    for key in d1.keys():
        if key in d2:
            inter[key] = f(d1[key], d2[key])
        else:
            diff[key] = d1[key]

    for key in d2:
        if key not in inter:
            diff[key] = d2[key]

    return inter, diff
