#!/usr/bin/env python

##  Module pyprimes.py
##
##  Copyright (c) 2012 Steven D'Aprano.
##
##  Permission is hereby granted, free of charge, to any person obtaining
##  a copy of this software and associated documentation files (the
##  "Software"), to deal in the Software without restriction, including
##  without limitation the rights to use, copy, modify, merge, publish,
##  distribute, sublicense, and/or sell copies of the Software, and to
##  permit persons to whom the Software is furnished to do so, subject to
##  the following conditions:
##
##  The above copyright notice and this permission notice shall be
##  included in all copies or substantial portions of the Software.
##
##  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
##  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
##  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
##  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
##  CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
##  TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
##  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


"""Generate and test for small primes using a variety of algorithms
implemented in pure Python.

This module includes functions for generating prime numbers, primality
testing, and factorising numbers into prime factors. Prime numbers are
positive integers with no factors other than themselves and 1.


Generating prime numbers
========================

To generate an unending stream of prime numbers, use the ``primes()``
generator function:

    primes():
        Yield prime numbers 2, 3, 5, 7, 11, ...


    >>> p = primes()
    >>> [next(p) for _ in range(10)]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


To efficiently generate pairs of (isprime(i), i) for integers i, use the
generator functions ``checked_ints()`` and ``checked_oddints()``:

    checked_ints()
        Yield pairs of (isprime(i), i) for i=0,1,2,3,4,5...

    checked_oddints()
        Yield pairs of (isprime(i), i) for odd i=1,3,5,7...


    >>> it = checked_ints()
    >>> [next(it) for _ in range(5)]
    [(False, 0), (False, 1), (True, 2), (True, 3), (False, 4)]


Other convenience functions wrapping ``primes()`` are:

    ------------------  ----------------------------------------------------
    Function            Description
    ------------------  ----------------------------------------------------
    nprimes(n)          Yield the first n primes, then stop.
    nth_prime(n)        Return the nth prime number.
    prime_count(x)      Return the number of primes less than or equal to x.
    primes_below(x)     Yield the primes less than or equal to x.
    primes_above(x)     Yield the primes strictly greater than x.
    primesum(n)         Return the sum of the first n primes.
    primesums()         Yield the partial sums of the prime numbers.
    ------------------  ----------------------------------------------------


Primality testing
=================

These functions test whether numbers are prime or not. Primality tests fall
into two categories: exact tests, and probabilistic tests.

Exact tests are guaranteed to give the correct result, but may be slow,
particularly for large arguments. Probabilistic tests do not guarantee
correctness, but may be much faster for large arguments.

To test whether an integer is prime, use the ``isprime`` function:

    isprime(n)
        Return True if n is prime, otherwise return False.


    >>> isprime(101)
    True
    >>> isprime(102)
    False


Exact primality tests are:

    isprime_naive(n)
        Naive and slow trial division test for n being prime.

    isprime_division(n)
        A less naive trial division test for n being prime.

    isprime_regex(n)
        Uses a regex to test if n is a prime number.

        .. NOTE:: ``isprime_regex`` should be considered a novelty
           rather than a serious test, as it is very slow.


Probabilistic tests do not guarantee correctness, but can be faster for
large arguments. There are two probabilistic tests:

    fermat(n [, base])
        Fermat primality test, returns True if n is a weak probable
        prime to the given base, otherwise False.

    miller_rabin(n [, base])
        Miller-Rabin primality test, returns True if n is a strong
        probable prime to the given base, otherwise False.


Both guarantee no false negatives: if either function returns False, the
number being tested is certainly composite. However, both are subject to false
positives: if they return True, the number is only possibly prime.


    >>> fermat(12400013)  # composite 23*443*1217
    False
    >>> miller_rabin(14008971)  # composite 3*947*4931
    False


Prime factorisation
===================

These functions return or yield the prime factors of an integer.

    factors(n)
        Return a list of the prime factors of n.

    factorise(n)
        Yield tuples (factor, count) for n.


The ``factors(n)`` function lists repeated factors:


    >>> factors(37*37*109)
    [37, 37, 109]


The ``factorise(n)`` generator yields a 2-tuple for each unique factor, giving
the factor itself and the number of times it is repeated:

    >>> list(factorise(37*37*109))
    [(37, 2), (109, 1)]


Alternative and toy prime number generators
===========================================

These functions are alternative methods of generating prime numbers. Unless
otherwise stated, they generate prime numbers lazily on demand. These are
supplied for educational purposes and are generally slower or less efficient
than the preferred ``primes()`` generator.

    --------------  --------------------------------------------------------
    Function        Description
    --------------  --------------------------------------------------------
    croft()         Yield prime numbers using the Croft Spiral sieve.
    erat(n)         Return primes up to n by the sieve of Eratosthenes.
    sieve()         Yield primes using the sieve of Eratosthenes.
    cookbook()      Yield primes using "Python Cookbook" algorithm.
    wheel()         Yield primes by wheel factorization.
    --------------  --------------------------------------------------------

    .. TIP:: In the current implementation, the fastest of these
       generators is aliased as ``primes()``.


These generators however are extremely slow, and should be considered as
examples of algorithms which should *not* be used, supplied as a horrible
warning of how *not* to calculate primes.

    --------------  --------------------------------------------------------
    Function            Description
    --------------  --------------------------------------------------------
    awful_primes    Yield primes very slowly by an awful algorithm.
    naive_primes1   Yield primes slowly by a naive algorithm.
    naive_primes2   Yield primes slowly by a less naive algorithm.
    trial_division  Yield primes slowly using trial division.
    turner          Yield primes very slowly using Turner's algorithm.
    --------------  --------------------------------------------------------

"""


from __future__ import division


import functools
import itertools
import random


# Module metadata.
__version__ = "0.1.1a"
__date__ = "2012-02-22"
__author__ = "Steven D'Aprano"
__author_email__ = "steve+python@pearwood.info"

__all__ = ['primes', 'checked_ints', 'checked_oddints', 'nprimes',
           'primes_above', 'primes_below', 'nth_prime', 'prime_count',
           'primesum', 'primesums', 'warn_probably', 'isprime', 'factors',
           'factorise',
           ]


# ============================
# Python 2.x/3.x compatibility
# ============================

# This module should support 2.5+, including Python 3.

try:
    next
except NameError:
    # No next() builtin, so we're probably running Python 2.5.
    # Use a simplified version (without support for default).
    def next(iterator):
        return iterator.next()

try:
    range = xrange
except NameError:
    # No xrange built-in, so we're almost certainly running Python3
    # and range is already a lazy iterator.
    assert type(range(3)) is not list

try:
    from itertools import ifilter as filter, izip as zip
except ImportError:
    # Python 3, where filter and zip are already lazy.
    assert type(filter(None, [1, 2])) is not list
    assert type(zip("ab", [1, 2])) is not list

try:
    from itertools import compress
except ImportError:
    # Must be Python 2.x, so we need to roll our own.
    def compress(data, selectors):
        """compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F"""
        return (d for d, s in zip(data, selectors) if s)

try:
    from math import isfinite
except ImportError:
    # Python 2.6 or older.
    try:
        from math import isnan, isinf
    except ImportError:
        # Python 2.5. Quick and dirty substitutes.
        def isnan(x):
            return x != x
        def isinf(x):
            return x - x != 0
    def isfinite(x):
        return not (isnan(x) or isinf(x))


# =====================
# Helpers and utilities
# =====================

def _validate_int(obj):
    """Raise an exception if obj is not an integer."""
    m = int(obj + 0)  # May raise TypeError.
    if obj != m:
        raise ValueError('expected an integer but got %r' % obj)


def _validate_num(obj):
    """Raise an exception if obj is not a finite real number."""
    m = obj + 0  # May raise TypeError.
    if not isfinite(m):
        raise ValueError('expected a finite real number but got %r' % obj)


def _base_to_bases(base, n):
    if isinstance(base, tuple):
        bases = base
    else:
        bases = (base,)
    for b in bases:
        _validate_int(b)
        if not 1 <= b < n:
            # Note that b=1 is a degenerate case which is always a prime
            # witness for both the Fermat and Miller-Rabin tests. I mention
            # this for completeness, not because we need to do anything
            # about it.
            raise ValueError('base %d out of range 1...%d' % (b, n-1))
    return bases


# =======================
# Prime number generators
# =======================

# The preferred generator to use is ``primes()``, which will be set to the
# "best" of these generators. (If you disagree with my judgement of best,
# feel free to use the generator of your choice.)


def erat(n):
    """Return a list of primes up to and including n.

    This is a fixed-size version of the Sieve of Eratosthenes, using an
    adaptation of the traditional algorithm.

    >>> erat(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> erat(10000) == list(primes_below(10000))
    True

    """
    _validate_int(n)
    # Generate a fixed array of integers.
    arr = list(range(n+1))
    # Cross out 0 and 1 since they aren't prime.
    arr[0] = arr[1] = None
    i = 2
    while i*i <= n:
        # Cross out all the multiples of i starting from i**2.
        for p in range(i*i, n+1, i):
            arr[p] = None
        # Advance to the next number not crossed off.
        i += 1
        while i <= n and arr[i] is None:
            i += 1
    return list(filter(None, arr))


def sieve():
    """Yield prime integers using the Sieve of Eratosthenes.

    This algorithm is modified to generate the primes lazily rather than the
    traditional version which operates on a fixed size array of integers.
    """
    # This is based on a paper by Melissa E. O'Neill, with an implementation
    # given by Gerald Britton:
    # http://mail.python.org/pipermail/python-list/2009-January/1188529.html
    innersieve = sieve()
    prevsq = 1
    table  = {}
    i = 2
    while True:
        # Note: this explicit test is slightly faster than using
        # prime = table.pop(i, None) and testing for None.
        if i in table:
            prime = table[i]
            del table[i]
            nxt = i + prime
            while nxt in table:
                nxt += prime
            table[nxt] = prime
        else:
            yield i
            if i > prevsq:
                j = next(innersieve)
                prevsq = j**2
                table[prevsq] = j
        i += 1


def cookbook():
    """Yield prime integers lazily using the Sieve of Eratosthenes.

    Another version of the algorithm, based on the Python Cookbook,
    2nd Edition, recipe 18.10, variant erat2.
    """
    # http://onlamp.com/pub/a/python/excerpt/pythonckbk_chap1/index1.html?page=2
    table = {}
    yield 2
    # Iterate over [3, 5, 7, 9, ...]. The following is equivalent to, but
    # faster than, (2*i+1 for i in itertools.count(1))
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        # Note: this explicit test is marginally faster than using
        # table.pop(i, None) and testing for None.
        if q in table:
            p = table[q]; del table[q]  # Faster than pop.
            x = p + q
            while x in table or not (x & 1):
                x += p
            table[x] = p
        else:
            table[q*q] = q
            yield q


def croft():
    """Yield prime integers using the Croft Spiral sieve.

    This is a variant of wheel factorisation modulo 30.
    """
    # Implementation is based on erat3 from here:
    #   http://stackoverflow.com/q/2211990
    # and this website:
    #   http://www.primesdemystified.com/
    # Memory usage increases roughly linearly with the number of primes seen.
    # dict ``roots`` stores an entry x:p for every prime p.
    for p in (2, 3, 5):
        yield p
    roots = {9: 3, 25: 5}  # Map d**2 -> d.
    primeroots = frozenset((1, 7, 11, 13, 17, 19, 23, 29))
    selectors = (1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0)
    for q in compress(
            # Iterate over prime candidates 7, 9, 11, 13, ...
            itertools.islice(itertools.count(7), 0, None, 2),
            # Mask out those that can't possibly be prime.
            itertools.cycle(selectors)
            ):
        # Using dict membership testing instead of pop gives a
        # 5-10% speedup over the first three million primes.
        if q in roots:
            p = roots[q]
            del roots[q]
            x = q + 2*p
            while x in roots or (x % 30) not in primeroots:
                x += 2*p
            roots[x] = p
        else:
            roots[q*q] = q
            yield q


def wheel():
    """Generate prime numbers using wheel factorisation modulo 210."""
    for i in (2, 3, 5, 7, 11):
        yield i
    # The following constants are taken from the paper by O'Neill.
    spokes = (2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6, 4, 2, 6, 4, 6,
        8, 4, 2, 4, 2, 4, 8, 6, 4, 6, 2, 4, 6, 2, 6, 6, 4, 2, 4, 6, 2,
        6, 4, 2, 4, 2, 10, 2, 10)
    assert len(spokes) == 48
    # This removes about 77% of the composites that we would otherwise
    # need to divide by.
    found = [(11, 121)]  # Smallest prime we care about, and its square.
    for incr in itertools.cycle(spokes):
        i += incr
        for p, p2 in found:
            if p2 > i:  # i must be a prime.
                found.append((i, i*i))
                yield i
                break
            elif i % p == 0:  # i must be composite.
                break
        else:  # This should never happen.
            raise RuntimeError("internal error: ran out of prime divisors")


# This is the preferred way of generating prime numbers. Set this to the
# fastest/best generator.
primes = croft


# === Algorithms to avoid ===

# The following algorithms are supplied for educational purposes, as toys,
# curios, or as terrible warnings on what NOT to use.
#
# None of these have acceptable performance; they are barely tolerable even
# for the first 100 primes.

def awful_primes():
    """Generate prime numbers naively, and REALLY slowly.

    This is about as awful as you can get while still being a straight-forward
    and unobfuscated implementation. What makes this particularly awful is
    that it doesn't stop testing for factors when it finds one, but
    pointlessly keeps testing.
    """
    i = 2
    yield i
    while True:
        i += 1
        composite = False
        for p in range(2, i):
            if i%p == 0:
                composite = True
        if not composite:  # It must be a prime.
            yield i


def naive_primes1():
    """Generate prime numbers naively and slowly.

    This is a bit better than awful_primes, as it short-circuits testing for
    composites. If it finds a single factor, it stops testing. Nevertheless,
    this is still terribly slow.
    """
    i = 2
    yield i
    while True:
        i += 1
        if all(i%p != 0 for p in range(2, i)):
            yield i


def naive_primes2():
    """Generate prime numbers naively and slowly.

    This is an incremental improvement over ``naive_primes1``, by only testing
    for odd factors.
    """
    yield 2
    i = 3
    yield i
    while True:
        i += 2
        if all(i%p != 0 for p in range(3, i, 2)):
            yield i


def trial_division():
    """Generate prime numbers slowly using a simple trial division algorithm.

    This uses three optimizations: we only test odd numbers for primality,
    we only test with prime factors, and that only up to the square root of
    the number being tested. This gives us asymptotic behaviour of
    O(N*sqrt(N)/(log N)**2) where N is the number of primes found.

    Despite these optimizations, this is still unacceptably slow, especially
    as the list of memorised primes grows.
    """
    yield 2
    primes = [2]
    i = 3
    while 1:
        it = itertools.takewhile(lambda p, i=i: p*p <= i, primes)
        if all(i%p != 0 for p in it):
            primes.append(i)
            yield i
        i += 2


def turner():
    """Yield prime numbers very slowly using Euler's sieve.

    The function is named for David Turner, who developed this implementation
    in a paper in 1975. Due to its simplicity, it has become very popular,
    particularly in Haskell circles where it is usually implemented as some
    variation of:

        primes = sieve [2..]
        sieve (p : xs) = p : sieve [x | x <- xs, x `mod` p > 0]

    This algorithm is often wrongly described as the Sieve of Eratosthenes,
    but it is not. Although simple, it is slow and inefficient, with
    asymptotic behaviour of O(N**2/(log N)**2), which is even worse than
    trial_division, and only marginally better than naive_primes. O'Neill
    calls this the "Sleight on Eratosthenes".
    """
    # References:
    #   http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    #   http://en.literateprograms.org/Sieve_of_Eratosthenes_(Haskell)
    #   http://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf
    #   http://www.haskell.org/haskellwiki/Prime_numbers
    nums = itertools.count(2)
    while True:
        prime = next(nums)
        yield prime
        nums = filter(lambda v, p=prime: (v % p) != 0, nums)


# =====================
# Convenience functions
# =====================

def checked_ints():
    """Yield tuples (isprime(i), i) for integers i=0, 1, 2, 3, 4, ...

    >>> it = checked_ints()
    >>> [next(it) for _ in range(6)]
    [(False, 0), (False, 1), (True, 2), (True, 3), (False, 4), (True, 5)]

    """
    oddnums = checked_oddints()
    yield (False, 0)
    yield next(oddnums)
    yield (True, 2)
    for t in oddnums:
        yield t
        yield (False, t[1]+1)


def checked_oddints():
    """Yield tuples (isprime(i), i) for odd integers i=1, 3, 5, 7, 9, ...

    >>> it = checked_oddints()
    >>> [next(it) for _ in range(6)]
    [(False, 1), (True, 3), (True, 5), (True, 7), (False, 9), (True, 11)]
    >>> [next(it) for _ in range(6)]
    [(True, 13), (False, 15), (True, 17), (True, 19), (False, 21), (True, 23)]

    """
    yield (False, 1)
    odd_primes = primes()
    _ = next(odd_primes)  # Skip 2.
    prev = 1
    for p in odd_primes:
        # Yield the non-primes between the previous prime and
        # the current one.
        for i in itertools.islice(itertools.count(prev + 2), 0, None, 2):
            if i >= p: break
            yield (False, i)
        # And yield the current prime.
        yield (True, p)
        prev = p


def nprimes(n):
    """Convenience function that yields the first n primes.

    >>> list(nprimes(10))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    """
    _validate_int(n)
    return itertools.islice(primes(), n)


def primes_above(x):
    """Convenience function that yields primes strictly greater than x.

    >>> next(primes_above(200))
    211

    """
    _validate_num(x)
    it = primes()
    # Consume the primes below x as fast as possible, then yield the rest.
    p = next(it)
    while p <= x:
        p = next(it)
    yield p
    for p in it:
        yield p


def primes_below(x):
    """Convenience function yielding primes less than or equal to x.

    >>> list(primes_below(20))
    [2, 3, 5, 7, 11, 13, 17, 19]

    """
    _validate_num(x)
    for p in primes():
        if p > x:
            return
        yield p


def nth_prime(n):
    """nth_prime(n) -> int

    Return the nth prime number, starting counting from 1. Equivalent to
    p-subscript-n in standard maths notation.

    >>> nth_prime(1)  # First prime is 2.
    2
    >>> nth_prime(5)
    11
    >>> nth_prime(50)
    229

    """
    # http://www.research.att.com/~njas/sequences/A000040
    _validate_int(n)
    if n < 1:
        raise ValueError('argument must be a positive integer')
    return next(itertools.islice(primes(), n-1, None))


def prime_count(x):
    """prime_count(x) -> int

    Returns the number of prime numbers less than or equal to x.
    It is also known as the Prime Counting Function, or pi(x).
    (Not to be confused with the constant pi = 3.1415....)

    >>> prime_count(20)
    8
    >>> prime_count(10000)
    1229

    The number of primes less than x is approximately x/(ln x - 1).
    """
    # See also:  http://primes.utm.edu/howmany.shtml
    # http://mathworld.wolfram.com/PrimeCountingFunction.html
    _validate_num(x)
    return sum(1 for p in primes_below(x))


def primesum(n):
    """primesum(n) -> int

    primesum(n) returns the sum of the first n primes.

    >>> primesum(9)
    100
    >>> primesum(49)
    4888

    The sum of the first n primes is approximately n**2*ln(n)/2.
    """
    # See:  http://mathworld.wolfram.com/PrimeSums.html
    # http://www.research.att.com/~njas/sequences/A007504
    _validate_int(n)
    return sum(nprimes(n))


def primesums():
    """Yield the partial sums of the prime numbers.

    >>> p = primesums()
    >>> [next(p) for _ in range(5)]  # primes 2, 3, 5, 7, 11, ...
    [2, 5, 10, 17, 28]

    """
    n = 0
    for p in primes():
        n += p
        yield n


# =================
# Primality testing
# =================

# Set this to a true value to have isprime(n) warn if the result is
# probabilistic; set it to a false value to skip the warning.
warn_probably = True


def isprime(n):
    """isprime(n) -> True|False

    Returns True if integer n is prime number, otherwise return False.

    For n less than approximately 341 trillion, ``isprime(n)`` is exact. Above
    that value, it is probabilistic with a vanishingly small chance of wrongly
    reporting a composite number as being prime. (It will never report a prime
    as composite.) The probability of a false positive is less than 1/10**24,
    or fewer than 1 time in a million trillion trillion tests.

    If the global variable ``warn_probably`` is true (the default), isprime
    will raise a warning when n is probably prime rather than certainly prime.
    """
    _validate_int(n)
    # Deal with trivial cases first.
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    elif n <= 7:  # 3, 5, 7
        return True
    bases = _choose_bases(n)
    flag = miller_rabin(n, bases)
    if flag and len(bases) > 7 and warn_probably:
        import warnings
        warnings.warn("number is only probably prime not certainly prime")
    return flag


def _choose_bases(n):
    """Choose appropriate bases for the Miller-Rabin primality test.

    If n is small enough, returns a tuple of bases which are provably
    deterministic for that n. If n is too large, return a mostly random
    selection of bases such that the chances of an error is less than
    1/4**40 = 8.2e-25.
    """
    # The Miller-Rabin test is deterministic and completely accurate for
    # moderate sizes of n using a surprisingly tiny number of tests.
    # See: Pomerance, Selfridge and Wagstaff (1980), and Jaeschke (1993)
    # http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    if n < 1373653:  # Blah, it's too hard to read big ints at a glance.
        # ~1.3 million
        bases = (2, 3)
    elif n < 9080191:  # ~9.0 million
        bases = (31, 73)
    elif n < 4759123141:  # ~4.7 billion
        # Note to self: checked up to approximately 394 million in 9 hours.
        bases = (2, 7, 61)
    elif n < 2152302898747:  # ~2.1 trillion
        bases = (2, 3, 5, 7, 11)
    elif n < 3474749660383:  # ~3.4 trillion
        bases = (2, 3, 5, 7, 11, 13)
    elif n < 341550071728321:  # ~341 trillion
        bases = (2, 3, 5, 7, 11, 13, 17)
    else:
        # n is too large, so we have to use a probabilistic test. There's no
        # harm in trying some of the lower values for base first.
        bases = (2, 3, 5, 7, 11, 13, 17) + tuple(
                    [random.randint(18, n-1) for _ in range(40)]
                    )
        # Note: we can always be deterministic, no matter how large N is, by
        # exhaustive testing against each i in the inclusive range
        # 1 ... min(n-1, floor(2*(ln N)**2)). We don't do this, because it is
        # expensive for large N, and of no real practical benefit.
    return bases


def isprime_naive(n):
    """Naive test for primes. Returns True if int n is prime, otherwise False.

    >>> isprime_naive(7)
    True
    >>> isprime_naive(8)
    False

    Naive, slow but thorough test for primality using unoptimized trial
    division. This function does far too much work, and consequently is very
    slow, but it is simple enough to verify by eye and can be used to check
    the results of faster algorithms. (At least for very small n.)
    """
    _validate_int(n)
    if n == 2:  return True
    if n < 2 or n % 2 == 0:  return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def isprime_division(n):
    """isprime_division(integer) -> True|False

    Exact primality test returning True if the argument is a prime number,
    otherwise False.

    >>> isprime_division(11)
    True
    >>> isprime_division(12)
    False

    This function uses trial division by the primes, skipping non-primes.
    """
    _validate_int(n)
    if n < 2:
        return False
    limit = n**0.5
    for divisor in primes():
        if divisor > limit: break
        if n % divisor == 0: return False
    return True


from re import match as _re_match

def isprime_regex(n):
    """isprime_regex(n) -> True|False

    Astonishingly, you can test whether a number is prime using a regex.
    It goes without saying that this is not efficient, and should be treated
    as a novelty rather than a serious implementation. It is O(N^2) in time
    and O(N) in memory: in other words, slow and expensive.
    """
    _validate_int(n)
    return not _re_match(r'^1?$|^(11+?)\1+$', '1'*n)
    # For a Perl version, see here:
    #   http://montreal.pm.org/tech/neil_kandalgaonkar.shtml
    # And for a Ruby version, here:
    #   http://www.noulakaz.net/weblog/2007/03/18/a-regular-expression-to-check-for-prime-numbers/


# === Probabilistic primality tests ===

def fermat(n, base=2):
    """fermat(n [, base]) -> True|False

    ``fermat(n, base)`` is a probabilistic test for primality which returns
    True if integer n is a weak probable prime to the given integer base,
    otherwise n is definitely composite and False is returned.

    ``base`` must be a positive integer between 1 and n-1 inclusive, or a
    tuple of such bases. By default, base=2.

    If ``fermat`` returns False, that is definite proof that n is composite:
    there are no false negatives. However, if it returns True, that is only
    provisional evidence that n is prime. For example:

    >>> fermat(99, 7)
    False
    >>> fermat(29, 7)
    True

    We can conclude that 99 is definitely composite, and state that 7 is a
    witness that 29 may be prime.

    As the Fermat test is probabilistic, composite numbers will sometimes
    pass a test, or even repeated tests:

    >>> fermat(3*11*17, 7)  # A pseudoprime to base 7.
    True

    You can perform multiple tests with a single call by passing a tuple of
    ints as ``base``. The number must pass the Fermat test for all the bases
    in order to return True. If any test fails, ``fermat`` will return False.

    >>> fermat(41041, (17, 23, 356, 359))  # 41041 = 7*11*13*41
    True
    >>> fermat(41041, (17, 23, 356, 359, 363))
    False

    If a number passes ``k`` Fermat tests, we can conclude that the
    probability that it is either a prime number, or a particular type of
    pseudoprime known as a Carmichael number, is at least ``1 - (1/2**k)``.
    """
    # http://en.wikipedia.org/wiki/Fermat_primality_test
    _validate_int(n)
    bases = _base_to_bases(base, n)
    # Deal with the simple deterministic cases first.
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    # Now the Fermat test proper.
    for a in bases:
        if pow(a, n-1, n) != 1:
            return False  # n is certainly composite.
    return True  # All of the bases are witnesses for n being prime.


def miller_rabin(n, base=2):
    """miller_rabin(integer [, base]) -> True|False

    ``miller_rabin(n, base)`` is a probabilistic test for primality which
    returns True if integer n is a strong probable prime to the given integer
    base, otherwise n is definitely composite and False is returned.

    ``base`` must be a positive integer between 1 and n-1 inclusive, or a
    tuple of such bases. By default, base=2.

    If ``miller_rabin`` returns False, that is definite proof that n is
    composite: there are no false negatives. However, if it returns True,
    that is only provisional evidence that n is prime:

    >>> miller_rabin(99, 7)
    False
    >>> miller_rabin(29, 7)
    True

    We can conclude from this that 99 is definitely composite, and that 29 is
    possibly prime.

    As the Miller-Rabin test is probabilistic, composite numbers will
    sometimes pass one or more tests:

    >>> miller_rabin(3*11*17, 103)  # 3*11*17=561, the 1st Carmichael number.
    True

    You can perform multiple tests with a single call by passing a tuple of
    ints as ``base``. The number must pass the Miller-Rabin test for each of
    the bases before it will return True. If any test fails, ``miller_rabin``
    will return False.

    >>> miller_rabin(41041, (16, 92, 100, 256))  # 41041 = 7*11*13*41
    True
    >>> miller_rabin(41041, (16, 92, 100, 256, 288))
    False

    If a number passes ``k`` Miller-Rabin tests, we can conclude that the
    probability that it is a prime number is at least ``1 - (1/4**k)``.
    """
    # http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    _validate_int(n)
    bases = _base_to_bases(base, n)
    # Deal with the trivial cases.
    if n < 2:
        return False
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    # Now perform the Miller-Rabin test proper.
    # Start by writing n-1 as 2**s * d.
    d, s = _factor2(n-1)
    for a in bases:
        if _is_composite(a, d, s, n):
            return False  # n is definitely composite.
    # If we get here, all of the bases are witnesses for n being prime.
    return True


def _factor2(n):
    """Factorise positive integer n as d*2**i, and return (d, i).

    >>> _factor2(768)
    (3, 8)
    >>> _factor2(18432)
    (9, 11)

    Private function used internally by ``miller_rabin``.
    """
    assert n > 0 and int(n) == n
    i = 0
    d = n
    while 1:
        q, r = divmod(d, 2)
        if r == 1:
            break
        i += 1
        d = q
    assert d%2 == 1
    assert d*2**i == n
    return (d, i)


def _is_composite(b, d, s, n):
    """_is_composite(b, d, s, n) -> True|False

    Tests base b to see if it is a witness for n being composite. Returns
    True if n is definitely composite, otherwise False if it *may* be prime.

    >>> _is_composite(4, 3, 7, 385)
    True
    >>> _is_composite(221, 3, 7, 385)
    False

    Private function used internally by ``miller_rabin``.
    """
    assert d*2**s == n-1
    if pow(b, d, n) == 1:
        return False
    for i in range(s):
        if pow(b, 2**i * d, n) == n-1:
            return False
    return True


# ===================
# Prime factorisation
# ===================

if __debug__:
    # Set _EXTRA_CHECKS to True to enable potentially expensive assertions
    # in the factors() and factorise() functions. This is only defined or
    # checked when assertions are enabled.
    _EXTRA_CHECKS = False


def factors(n):
    """factors(integer) -> [list of factors]

    Returns a list of the (mostly) prime factors of integer n. For negative
    integers, -1 is included as a factor. If n is 0 or 1, [n] is returned as
    the only factor. Otherwise all the factors will be prime.

    >>> factors(-693)
    [-1, 3, 3, 7, 11]
    >>> factors(55614)
    [2, 3, 13, 23, 31]

    """
    _validate_int(n)
    result = []
    for p, count in factorise(n):
        result.extend([p]*count)
    if __debug__:
        # The following test only occurs if assertions are on.
        if _EXTRA_CHECKS:
            prod = 1
            for x in result:
                prod *= x
            assert prod == n, ('factors(%d) failed multiplication test' % n)
    return result


def factorise(n):
    """factorise(integer) -> yield factors of integer lazily

    >>> list(factorise(3*7*7*7*11))
    [(3, 1), (7, 3), (11, 1)]

    Yields tuples of (factor, count) where each factor is unique and usually
    prime, and count is an integer 1 or larger.

    The factors are prime, except under the following circumstances: if the
    argument n is negative, -1 is included as a factor; if n is 0 or 1, it
    is given as the only factor. For all other integer n, all of the factors
    returned are prime.
    """
    _validate_int(n)
    if n in (0, 1, -1):
        yield (n, 1)
        return
    elif n < 0:
        yield (-1, 1)
        n = -n
    assert n >= 2
    for p in primes():
        if p*p > n: break
        count = 0
        while n % p == 0:
            count += 1
            n //= p
        if count:
            yield (p, count)
    if n != 1:
        if __debug__:
            # The following test only occurs if assertions are on.
            if _EXTRA_CHECKS:
                assert isprime(n), ('failed isprime test for %d' % n)
        yield (n, 1)



if __name__ == '__main__':
    import doctest
    doctest.testmod()

