"""
Constraints:
1 <= nums.length <= 1500
1 <= nums[i] <= 1500

Hints
What is the maximum possible XOR value achievable by any triplet?
Let the maximum possible XOR value be stored in max_xor.
For each index i, consider all pairs of indices (j, k) such that i <= j <= k. For each such pair, compute the triplet XOR as nums[i] XOR nums[j] XOR nums[k].
You can optimize the calculation by precomputing or reusing intermediate XOR results. For example, after fixing an index i, compute XORs of pairs (j, k) in O(n2) time instead of checking all three indices independently.
Finally, count the number of unique XOR values obtained from all triplets.

Copied without being able to understand completely despite trying:
https://leetcode.com/problems/number-of-unique-xor-triplets-ii/solutions/6643945/python3-8-lines-iteration-ts-99-80-by-sp-go03
Was able to understand only after using ChatGPT

"""
class Solution:
    def uniqueXorTriplets(self, V: List[int]) -> int:
        X2 = {0}                                # XOR of pairs
        X3 = set(V)                             # XOR of triplets

        k = 1 << max(V).bit_length()

        while V:
            v = V.pop()                         # pop :: prevents reuse below

            X3 |= {v ^ x2 for x2 in X2}         # existing pair ^ current value => triplet
            X2 |= {v ^ vv for vv in V}          # any value ^ current value => pair
            
            if len(X3) == k: break
        
        return len(X3)