class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        """
        Find all integers in the range [low, high] that have sequential digits.
        Sequential digits means every digit in the number is one more than the previous digit.
      
        Args:
            low: Lower bound of the range (inclusive)
            high: Upper bound of the range (inclusive)
          
        Returns:
            A sorted list of integers with sequential digits
        """
        result = []
      
        # Iterate through possible starting digits (1-8)
        # Starting digit can't be 9 since we need at least one more digit after it
        for start_digit in range(1, 9):
            current_number = start_digit
          
            # Build numbers by appending consecutive digits
            # Next digit must be start_digit + 1, start_digit + 2, etc.
            for next_digit in range(start_digit + 1, 10):
                # Append the next sequential digit to current number
                current_number = current_number * 10 + next_digit
              
                # Check if the formed number is within the given range
                if low <= current_number <= high:
                    result.append(current_number)
      
        # Sort the result list before returning
        return sorted(result)
