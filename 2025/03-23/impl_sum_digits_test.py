"""
백준 11720 - 숫자의 합
https://www.acmicpc.net/problem/11720

# 입력 예시 (sys.stdin.readline 사용 시):
import sys

n = int(sys.stdin.readline())
digits = sys.stdin.readline().strip()
"""

def sum_digits(n, digits_str):
    total_sum = 0
    for n in digits_str :
        print(n)
        total_sum += int(n)

    # return sum(int(ch) for ch in digits_str)
    return total_sum


def test_sum_digits():
    tests = [
        {"index": 1, "n": 1, "digits": "1", "want": 1},
        {"index": 2, "n": 5, "digits": "54321", "want": 15},
        {"index": 3, "n": 25, "digits": "7000000000000000000000000", "want": 7},
        {"index": 4, "n": 3, "digits": "000", "want": 0},
        {"index": 5, "n": 4, "digits": "9999", "want": 36},
    ]

    for t in tests:
        got = sum_digits(t["n"], t["digits"])
        if got != t["want"]:
            print(f"❌ 실패: 테스트 {t['index']} - sum_digits({t['n']}, '{t['digits']}') = {got}; expected {t['want']}")
        else:
            print(f"✅ 성공: 테스트 {t['index']} - got = {got}")


# 테스트 실행
if __name__ == "__main__":
    test_sum_digits()
