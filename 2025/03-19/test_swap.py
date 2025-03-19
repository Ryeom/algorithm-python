def swap(a, b):
    return b,a

# 테스트
def test_swap():
    a, b = 5, 10
    a, b = swap(a, b)
    assert a == 10 and b == 5, f"Expected 10, 5 but got {a}, {b}"

    print("모든 테스트 케이스가 통과했습니다!")

# 테스트 실행
test_swap()
