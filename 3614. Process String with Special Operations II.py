class Solution:
    def processStr(self, s: str, k: int) -> str:
        # First pass, identify the final length of the string
        l = 0
        for c in s:
            if c == '*':
                if l > 0:
                    l -= 1
            elif c == '#':
                l *= 2
            elif c == '%':
                pass
            else:
                l += 1

        # We must be looking for position 'k' within the length 'l',
        # otherwise return undefined char
        if k >= l:
            return '.'

        # Second pass: Update `k`, and `l` which dynamically tracks
        # the length of the string while backtracking.
        ptr = k
        for c in s[::-1]:
            if c == '*':
                l += 1
            elif c == '#':
                if ptr >= l // 2:
                    ptr -= l // 2
                l = l // 2
            elif c == '%':
                # even length string: let's say l == 2, then 0<=>1
                # odd length string: let's say l == 3, then 0<=>2, 1 unchanged
                # either way:
                ptr = (l - 1) - ptr
            else:
                # Early return: the character was added here
                if l == ptr + 1:
                    return c
                l -= 1
        return s[ptr]