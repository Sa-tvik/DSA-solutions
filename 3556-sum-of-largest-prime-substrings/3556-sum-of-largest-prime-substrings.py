class Solution(object):
    def sumOfLargestPrimes(self, s):
        """
        :type s: str
        :rtype: int
        """
        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True  # 2 and 3 are prime
        
            if n % 2 == 0 or n % 3 == 0:
                return False
        
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
        
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

            
