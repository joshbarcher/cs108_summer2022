# my favorite numbers
nums = [-10, 0, 2, 7, 42, 719]
print("Before:", nums)

# loop over the list and increment all numbers in the list

# this is the wrong type of for loop
# for number in nums:
#     number += 1
#     print("Changed number:", number)

# instead loop over indices
for index in range(0, len(nums)):
    number = nums[index]
    number += 1
    print("Changed number:", number)

    # save the number that was incremented
    nums[index] = number

print("After:", nums)

