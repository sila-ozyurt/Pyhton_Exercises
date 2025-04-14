class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # Create a list to store the maximum substring length for each character.
        dp = [0] * 150
        # Initialize a variable to store the length of the longest ideal string.
        max_len = 1

        # Iterate through each character in the string.
        for c in s:
            # Iterate over current-2,current+2
            for i in range(ord(c) - k, ord(c) + k + 1):
                # Continue only if the character falls within the range of lowercase letters.
                if ord('a') <= i <= ord('z'):
                    # Compare the substring length for the current character with the substring length
                    # for the characters in the range, and update the maximum substring length accordingly.
                    dp[ord(c)] = max(dp[ord(c)], dp[i])

            # Calculate the substring length for the current character and update the dp array.
            dp[ord(c)] += 1
            # Update the maximum substring length.
            max_len = max(max_len, dp[ord(c)])

        # Return the length of the longest ideal string.
        return max_len
    
