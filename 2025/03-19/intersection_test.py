def intersection(arr1, arr2):
    a1 = set(arr1)
    a2 = set(arr2)
    return sorted(a1& a2)  # 임시값

# 테스트 코드
def test_intersection():
    # 예시 테스트 케이스
    arr1 = [1, 2, 2, 1]
    arr2 = [2, 2]
    result = intersection(arr1, arr2)
    assert result == [2], f"Expected [2], but got {result}"

    arr1 = [4, 9, 5]
    arr2 = [9, 4, 9, 8, 4]
    result = intersection(arr1, arr2)
    assert result == [4, 9], f"Expected [4, 9], but got {result}"

    # 추가 테스트 케이스
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    result = intersection(arr1, arr2)
    assert result == [], f"Expected [], but got {result}"

    print("모든 테스트 케이스가 통과했습니다!")

# 테스트 실행
test_intersection()
