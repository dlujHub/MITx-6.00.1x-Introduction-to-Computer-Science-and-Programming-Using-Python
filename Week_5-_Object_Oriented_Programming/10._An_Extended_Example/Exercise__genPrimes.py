# Exercise: genPrimes
# 5/5 points (graded)
# ESTIMATED TIME TO COMPLETE: 10 minutes

# Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

def genPrimes():
    list_primes = [2]
    yield list_primes[0]
    x = 3
    while True:
        if all(x % p != 0 for p in list_primes):
            list_primes.append(x)
        if list_primes[-1] == x:
            yield list_primes[-1]
        x += 1

# Correct
