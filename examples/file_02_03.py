# Алгоритмы поиска

# Бинарный поиск

nums = [2, 8, 10, 15, 25, 76, 78, 98]
target = 76

left = 0
right = len(nums) - 1

while left < right:
    middle = (left + right) // 2

    if nums[middle] == target:
        print(middle)
        break

    if nums[middle] > target:
        right = middle - 1  # 2
    elif nums[middle] < target:
        left = middle + 1  # 4
