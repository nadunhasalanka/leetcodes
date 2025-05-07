def longest_consecutive(nums):
    if not nums:
        return 0, []

    num_set = set(nums)
    longest_streak = 0
    longest_sequence = []

    for num in num_set:
        if num - 1 not in num_set:  # Check if it's the start of a sequence
            current_num = num
            current_streak = 1
            current_sequence = [current_num]

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
                current_sequence.append(current_num)

            if current_streak > longest_streak:
                longest_streak = current_streak
                longest_sequence = current_sequence

    return longest_streak, longest_sequence

# Test code
nums = [100, 4, 200, 1, 3, 2]
length, sequence = longest_consecutive(nums)
print(f"Length of longest consecutive sequence: {length}")  # Output: 4
print(f"Longest consecutive sequence: {sequence}")  # Output: [1, 2, 3, 4]
