class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        all_combs = []
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        def backtrack(curr_str, idx):
            #base case
            if len(curr_str) == len(digits):
                all_combs.append(''.join(curr_str[:]))
                return
            curr_possible_letters = digit_map[digits[idx]]
            for letter in curr_possible_letters:
                curr_str.append(letter)
                backtrack(curr_str, idx+1)
                curr_str.pop()
                
        backtrack([],0)
        return all_combs
                