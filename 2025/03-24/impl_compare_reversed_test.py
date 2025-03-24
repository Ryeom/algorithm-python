"""
숫자 뒤집기와 비교 문제
"""


def compare_reversed(a, b):
    a = int(a[::-1])
    b = int(b[::-1])
    return a if a > b else b


def test_compare_reversed():
    tests = [
        {"index": 1, "a": "734", "b": "893", "want": 437},
        {"index": 2, "a": "100", "b": "1", "want": 1},
        {"index": 3, "a": "123", "b": "321", "want": 321},
        {"index": 4, "a": "111", "b": "111", "want": 111},
        {"index": 5, "a": "987", "b": "789", "want": 987},
    ]

    for t in tests:
        got = compare_reversed(t["a"], t["b"])
        if got != t["want"]:
            print(f"❌ 실패: 테스트 {t['index']} - compare_reversed({t['a']}, {t['b']}) = {got}; expected {t['want']}")
        else:
            print(f"✅ 성공: 테스트 {t['index']} - got = {got}")


if __name__ == "__main__":
    test_compare_reversed()
