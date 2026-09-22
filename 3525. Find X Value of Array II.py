class Solution:
    def resultArray(self, nums: list[int], k: int, q: list[list[int]]) -> list[int]:
        n = len(nums)

        # tree[node] = [product modulo k, prefix product counts]
        #
        # pref[r] = number of non-empty prefixes of this segment
        #           whose product % k == r

        tree = [None] * (4 * n)

        def make_node(value):
            prod = value % k
            pref = [0] * k
            pref[prod] = 1
            return prod, pref

        def merge(left, right):
            left_prod, left_pref = left
            right_prod, right_pref = right

            prod = (left_prod * right_prod) % k
            pref = left_pref[:]

            # Prefixes entirely inside right segment.
            # Their product gets multiplied by whole left segment.
            for r in range(k):
                count = right_pref[r]
                if count:
                    nr = (left_prod * r) % k
                    pref[nr] += count

            return prod, pref

        def build(node, l, r):
            if l == r:
                tree[node] = make_node(nums[l])
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, idx, value):
            if l == r:
                tree[node] = make_node(value)
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, value)
            else:
                update(node * 2 + 1, mid + 1, r, idx, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        ans = []

        for idx, val, s, x in q:
            nums[idx] = val

            update(1, 0, n - 1, idx, val)

            _, pref = query(1, 0, n - 1, s, n - 1)

            ans.append(pref[x])

        return ans