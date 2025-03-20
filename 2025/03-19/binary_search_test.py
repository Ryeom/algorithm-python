def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target :
            return mid
        elif arr[mid] < target:
            left = mid +1
        else:
            right = mid -1
    return -1  # 임시값

# 테스트 코드
def test_binary_search():
    # 예시 테스트 케이스
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    result = binary_search(arr, target)
    assert result == 4, f"Expected 4, but got {result}"

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 10
    result = binary_search(arr, target)
    assert result == -1, f"Expected -1, but got {result}"

    # 추가 테스트 케이스
    arr = [1, 2, 3, 4, 5]
    target = 3
    result = binary_search(arr, target)
    assert result == 2, f"Expected 2, but got {result}"

    print("모든 테스트 케이스가 통과했습니다!")

# 테스트 실행
test_binary_search()
