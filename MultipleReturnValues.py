def min_max(nums):
    result = []
    for number in nums:
        result.append(number + 2)
    return result
       
nums = [3, 7, 1, 9]
print(min_max(nums))