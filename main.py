from typing import List

# Get user input as a list of integers
nums_input = input("Enter nums list separated by spaces: ")
nums = [int(x) for x in nums_input.split()]

# Get user input for the target number as an integer
target = int(input("Enter target number: "))

# Define the twoSum function
def twoSum(nums: List[int], target: int) -> List[int]:
    # Your twoSum logic here
    result = []
    # Example logic to find two numbers that sum to the target
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result = [i, j]
                break
    return result

# Call the twoSum function with user input
result = twoSum(nums, target)

# Print the result
print("Indices of the two numbers that sum to the target:", result)
