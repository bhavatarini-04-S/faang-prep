class Solution:
    def minPartitions(self, n: str) -> int:
        """
        Find the minimum number of positive deci-binary numbers needed to sum up to n.
      
        A deci-binary number is a decimal number where each digit is either 0 or 1.
        The key insight: the minimum number of partitions equals the maximum digit in n.
      
        Args:
            n: A string representation of a positive integer
          
        Returns:
            The minimum number of deci-binary numbers needed
        """
        # Find the maximum digit in the string representation of n
        # This works because each deci-binary number can contribute at most 1 to each digit position
        # Therefore, we need at least as many numbers as the largest digit value
        max_digit = max(n)
      
        # Convert the character digit to integer and return
        return int(max_digit)