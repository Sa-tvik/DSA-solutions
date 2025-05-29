class Solution(object):
    def sumOfLargestPrimes(self, s):
        """
        :type s: str
        :rtype: int
        """
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        primes = set()
        n = len(s)

        for i in range(n):
            temp = 0
            for j in range(i, n):
                temp = temp * 10 + int(s[j])
                if is_prime(temp):
                    primes.add(temp)

        primes = sorted(primes)
        if len(primes) < 3:
            return sum(primes)
        return sum(primes[-3:])

            
