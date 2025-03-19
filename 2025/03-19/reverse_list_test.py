def reverse_list(numbers):
    # TODO: 여기에 코드를 작성하세요.
    return numbers[len(numbers):0]  # 임시값

# 테스트 코드
def test_reverse_list():
    # 예시 테스트 케이스
    numbers = [1, 2, 3, 4, 5]
    result = reverse_list(numbers)
    assert result == [5, 4, 3, 2, 1], f"Expected [5, 4, 3, 2, 1], but got {result}"

    numbers = [10, 20, 30]
    result = reverse_list(numbers)
    assert result == [30, 20, 10], f"Expected [30, 20, 10], but got {result}"

    # 추가 테스트 케이스
    numbers = [1]
    result = reverse_list(numbers)
    assert result == [1], f"Expected [1], but got {result}"

    print("모든 테스트 케이스가 통과했습니다!")

# 테스트 실행
test_reverse_list()
