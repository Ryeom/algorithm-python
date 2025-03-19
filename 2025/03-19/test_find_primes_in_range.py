import math


def find_primes_in_range(start, end):
    res = []
    for i in range(start, end):
        if is_prime(i):
            res.append(i)
    return res

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number % i ==0:
            return False
    return True



# 테스트
def test_find_primes_in_range():
    result = find_primes_in_range(10, 50)
    assert result == [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47], f"Expected primes in range, but got {result}"

    print("모든 테스트 케이스가 통과했습니다!")

# 테스트 실행
test_find_primes_in_range()
