class Solution:
    def minimumPushes(self, word: str) -> int:
        # Step 1: Count frequencies
        freq = Counter(word)

        # Step 2: Create a max heap
        max_heap = []

        for f in freq.values():
            heapq.heappush(max_heap, -f)   # negative because heapq is a min-heap

        ans = 0
        index = 0

        # Step 3: Process highest frequencies first
        while max_heap:

            frequency = -heapq.heappop(max_heap)

            presses = index // 8 + 1

            ans += frequency * presses

            index += 1

        return ans

        # from collections import Counter
        # d = dict(Counter(word))
        # freq = sorted(d.values(),reverse=True)
        # ans = 0
        # for i,f in enumerate(freq):
        #     press = i//8 + 1
        #     ans = ans + (f*press)
        # return ans