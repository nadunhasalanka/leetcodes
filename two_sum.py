"""
LeetCode Problem: Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

def two_sum(nums, target):
    """
    Time Complexity: O(n) where n is the length of nums
    Space Complexity: O(n) for the hash map
    
    Args:
        nums: List of integers
        target: Integer target sum
    
    Returns:
        List of two indices whose values sum to target
    """
    # Create a hash map to store numbers and their indices
    num_map = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement (the number needed to reach target)
        complement = target - num
        
        # If the complement exists in our map, we found our answer
        if complement in num_map:
            return [num_map[complement], i]
        
        # Otherwise, add the current number to our map
        num_map[num] = i
    
    # If no solution is found (though the problem guarantees one)
    return None

# Example usage
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")
    print(f"Explanation: Because nums[{result[0]}] + nums[{result[1]}] == {target}, we return {result}.")
