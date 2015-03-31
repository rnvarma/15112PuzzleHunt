# Sample Solution

```python
# This version avoids if statements and "and".
# This might be a bit too hard. Also, we haven't covered
# DeMorgan's Law in class, technically.
def isPrime(n):
    isBigEnough = n > 1
    isTwo = (n == 2)
    maxFactor = int(round(n**0.5))
    thereIsADivisor = (n % 2 == 0)
    for possibleFactor in xrange(3, maxFactor+1, 2):
        thereIsADivisor = thereIsADivisor or (n % possibleFactor == 0)
    return not((thereIsADivisor) or not(isBigEnough)) or isTwo

# An alternative solution
def isPrimeSol2(n):
    while n < 1:
        return False
    while n == 2:
        return True
    maxFactor = int(round(n ** 0.5))
    for possibleFactor in xrange(3, maxFactor+1, 2):
        while n % possibleFactor == 0:
            return False
    return True

def testIsPrime():
    print "Testing isPrime...",
    assert(isPrime(2))
    assert(isPrime(3))
    assert(isPrime(5))
    assert(isPrime(7))
    assert(isPrime(11))
    assert(isPrime(13))
    # assert(not isPrime(-1))
    assert(not isPrime(0))
    assert(not isPrime(1))
    assert(not isPrime(4))
    assert(not isPrime(10))
    print "Passed!"

testIsPrime()
```
