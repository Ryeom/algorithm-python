def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return -1

# 테스트 코드
def test_binary_search():
    # 예시 테스트 케이스
    nums = [-10, -5, 0, 3, 7, 9, 15]
    target = 3
    result = binary_search(nums, target)
    assert result == 3, f"Expected 3, but got {result}"

    nums = [-10, -5, 0, 3, 7, 9, 15]
    target = 8
    result = binary_search(nums, target)
    assert result == -1, f"Expected -1, but got {result}"

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7
    result = binary_search(nums, target)
    assert result == 6, f"Expected 6, but got {result}"

    nums = [2, 4, 6, 8, 10, 12, 14, 16]
    target = 5
    result = binary_search(nums, target)
    assert result == -1, f"Expected -1, but got {result}"

    print("모든 테스트 케이스가 통과했습니다!")

# 테스트 실행
test_binary_search()
