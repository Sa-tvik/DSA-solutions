class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def isPrime(i):
            if i <= 1:
                return False
            if i == 2:
                return True
            if i % 2 == 0:
                return False
            for j in range(3, int(math.sqrt(i)) + 1, 2):
                if i % j == 0:
                    return False
            return True

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        for count in freq.values():
            if isPrime(count):
                return True
        return False