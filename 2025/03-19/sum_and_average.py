def sum_and_average(numbers):
    total = 0
    for n in numbers:
        total += n

    return total, round(total / len(numbers),2)  # 임시값

# 테스트
def test_sum_and_average():
    numbers = [10, 20, 30, 40, 50]
    total, avg = sum_and_average(numbers)
    assert total == 150, f"Expected total 150, but got {total}"
    assert round(avg, 2) == 30.0, f"Expected avg 30.0, but got {avg}"

    print("모든 테스트 케이스가 통과했습니다!")

# 테스트 실행
test_sum_and_average()
