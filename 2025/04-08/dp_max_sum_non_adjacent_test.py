def max_non_adjacent_sum(houses):
    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]

    n = len(houses)
    dp = [0] * n
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])

    return dp[-1]


# 테스트 코드
def test_max_non_adjacent_sum():
    tests = [
        {"index": 1, "nums": [3, 2, 5, 10, 7], "want": 15},
        {"index": 2, "nums": [5, 5, 10, 100, 10, 5], "want": 110},
        {"index": 3, "nums": [3, 2, 7, 10], "want": 13},
        {"index": 4, "nums": [3, 2, 5], "want": 8},
        {"index": 5, "nums": [5], "want": 5},
        {"index": 6, "nums": [0, 0, 0, 0], "want": 0},
        {"index": 7, "nums": [1, 2, 3, 1], "want": 4},
        {"index": 8, "nums": [2, 1, 4, 9], "want": 11},
        {"index": 9, "nums": [100, 1, 1, 100], "want": 200},
        {"index": 10, "nums": [10, 5, 15, 20, 2, 30], "want": 60},
    ]

    for t in tests:
        got = max_non_adjacent_sum(t["nums"])
        if got != t["want"]:
            print(f"❌ 실패: 테스트 {t['index']} - max_non_adjacent_sum({t['nums']}) = {got}; expected {t['want']}")
        else:
            print(f"✅ 성공: 테스트 {t['index']} - got = {got}")

# 테스트 실행
test_max_non_adjacent_sum()
