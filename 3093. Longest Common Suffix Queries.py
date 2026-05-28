from bisect import bisect_left
from math import inf

class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        """
        Non-Trie solution.

        Idea:
        1) Reverse every word.
           Longest common suffix becomes longest common prefix.

        2) Sort reversed container words lexicographically.
           Strings with the same prefix become a contiguous block.

        3) For each query:
           - reverse it
           - find the maximum LCP with any container word
             using only the neighbors around its insertion point
           - then find the whole prefix block of that length
           - among that block, pick the shortest word
             (and if tie, the earliest index)

        We use a segment tree to answer:
            "which container word is best in a sorted interval?"
        where "best" means:
            smaller length first,
            then smaller original index.
        """

        # ------------------------------------------------------------
        # 1) Reverse all container words and keep:
        #    - reversed string
        #    - original length
        #    - original index
        #
        # We sort by reversed string, because suffix matching on the
        # original words becomes prefix matching on reversed words.
        # ------------------------------------------------------------
        container = []
        for idx, w in enumerate(wordsContainer):
            container.append((w[::-1], len(w), idx))

        container.sort(key=lambda x: x[0])

        rev_words = [x[0] for x in container]

        # best_info[i] = (length, original_index)
        # This is what we want to minimize inside a prefix block.
        best_info = [(x[1], x[2]) for x in container]

        n = len(container)

        # ------------------------------------------------------------
        # 2) Segment tree for range minimum on (length, index)
        #    Python tuple comparison works exactly how we want:
        #       (len1, idx1) < (len2, idx2)
        #    means smaller length first, then smaller index.
        # ------------------------------------------------------------
        size = 1
        while size < n:
            size *= 2

        seg = [(inf, inf)] * (2 * size)

        for i in range(n):
            seg[size + i] = best_info[i]

        for i in range(size - 1, 0, -1):
            seg[i] = min(seg[2 * i], seg[2 * i + 1])

        def query(l, r):
            """
            Return the best (length, index) in container[l..r].
            """
            l += size
            r += size
            ans = (inf, inf)

            while l <= r:
                if l % 2 == 1:
                    ans = min(ans, seg[l])
                    l += 1
                if r % 2 == 0:
                    ans = min(ans, seg[r])
                    r -= 1
                l //= 2
                r //= 2

            return ans

        # ------------------------------------------------------------
        # Helper: longest common prefix length of a and b
        # ------------------------------------------------------------
        def lcp(a, b):
            i = 0
            limit = min(len(a), len(b))
            while i < limit and a[i] == b[i]:
                i += 1
            return i

        # ------------------------------------------------------------
        # 3) For each query:
        #
        #    - reverse it
        #    - find the maximum LCP with any container word
        #      (it is enough to check the two neighbors around
        #       the insertion position in sorted order)
        #    - then find the full block of words having that prefix
        #    - query the segment tree on that interval to pick the best
        # ------------------------------------------------------------
        ans = []

        for q in wordsQuery:
            rq = q[::-1]

            # insertion position of rq in the sorted reversed container
            pos = bisect_left(rev_words, rq)

            # maximum LCP with any word is achieved by one of the
            # two neighbors around the insertion point
            best_l = 0
            if pos < n:
                best_l = max(best_l, lcp(rev_words[pos], rq))
            if pos > 0:
                best_l = max(best_l, lcp(rev_words[pos - 1], rq))

            # prefix of the query that must match the answer
            prefix = rq[:best_l]

            # all container words with this prefix form a contiguous block
            # in the sorted reversed array
            left = bisect_left(rev_words, prefix)
            right = bisect_left(rev_words, prefix + "{") - 1
            # '{' comes right after 'z' in ASCII,
            # so prefix + '{' is the first string that is strictly larger
            # than any lowercase string starting with prefix.

            # pick the best candidate in that whole block:
            #   1) smallest length
            #   2) earliest original index
            _, idx = query(left, right)
            ans.append(idx)

        return ans