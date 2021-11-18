# def binarySearchRecursive(sequence, x, left, right):
#         if left > right:
#             return False
#         mid = (left+right)//2
#         print('mid', sequence[mid])
#
#         if x == sequence[mid]:
#             return mid
#         elif x < sequence[mid]:
#             return binarySearchRecursive(sequence, x, left, mid - 1)
#         elif x > sequence[mid]:
#             return binarySearchRecursive(sequence, x, mid + 1, right)
#
#
# if __name__ == "__main__":
#     sample = [1, 2, 5, 6, 8, 10, 50, 70, 75, 77, 78, 79, 80, 81, 82, 85]
#     x = 77
#     print('Index of number ', x, 'is equal to ', binarySearchRecursive(sample, x, 0, len(sample) - 1))


def binarySearch(nums, target, left , right):

    middle = 0

    while left <= right:
        middle = (right + left) // 2


        if target == nums[middle]:
            return middle

        elif target > nums[middle]:
            low = middle + 1


        else:
            high = middle - 1


    return False


target = 2
nums = [-6, -4, -1, 0, 2, 4, 5, 6, 7, 9]
print(nums)
print(binarySearch(nums, target, 0, len(nums) - 1))