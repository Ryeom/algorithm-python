
def find_max_min(numbers):
    min_num = min(numbers)
    max_num = max(numbers)
    return max_num, min_num  # 임시값

def test_find_max_min():
    # 예시 테스트 케이스
    numbers = [3, 5, 1, 9, 2]
    max_num, min_num = find_max_min(numbers)
    assert max_num == 9, f"Expected max 9, but got {max_num}"
    assert min_num == 1, f"Expected min 1, but got {min_num}"

    # 추가 테스트 케이스
    numbers = [0, 0, 0, 0, 0]
    max_num, min_num = find_max_min(numbers)
    assert max_num == 0, f"Expected max 0, but got {max_num}"
    assert min_num == 0, f"Expected min 0, but got {min_num}"

    numbers = [1, -5, 3, 7, 2]
    max_num, min_num = find_max_min(numbers)
    assert max_num == 7, f"Expected max 7, but got {max_num}"
    assert min_num == -5, f"Expected min -5, but got {min_num}"

    print("모든 테스트 케이스가 통과했습니다!")

# 테스트 실행
test_find_max_min()
