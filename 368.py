def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Sort the array to ensure divisibility can be checked in ascending order
        nums.sort()
        n = len(nums)
        # Initialize a list to keep track of the longest subset ending at each index
        dp = [1] * n
        max_index = 0 # To track the index at which the largest divisible subset ends
      
        # Build up the dp array with the length of each longest divisible subset
        for i in range(n):
            for j in range(i):
                # Check if the current number is divisible by the j-th number
                if nums[i] % nums[j] == 0:
                    # Update the dp[i] to the maximum length achievable
                    dp[i] = max(dp[i], dp[j] + 1)
            # Update the index of the largest divisible subset if a new max is found
            if dp[max_index] < dp[i]:
                max_index = i
      
        # The size of the largest divisible subset
        subset_size = dp[max_index]
        # Start from the end element of the largest subset
        current_index = max_index
        # List to store the largest divisible subset
        largest_subset = []
      
        # Backtrack from the largest index found to build the subset
        while subset_size:
            # If the current number divides the number at max_index and its dp value
            # corresponds to the current subset size, add it to the result
            if nums[max_index] % nums[current_index] == 0 and dp[current_index] == subset_size:
                largest_subset.append(nums[current_index])
                # Update the max_index and decrement the size for next numbers
                max_index, subset_size = current_index, subset_size - 1
            # Move one index backwards
            current_index -= 1
      
        # Return the largest divisible subset in the original order
        return largest_subset