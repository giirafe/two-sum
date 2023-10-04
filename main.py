from typing import List

# nums_input = input("Enter nums list separated by spaces: ")
# nums = [int(x) for x in nums_input.split()]
# target = int(input("Enter target number: "))

nums = [3,2,4]
target = 6

# Define the twoSum function
def twoSum(nums: List[int], target: int) -> List[int]:
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result = [i, j]
                break

    return result

result = twoSum(nums, target)

# Print the result
print("Indices of the two numbers that sum to the target:", result)
