def count_subset_sum(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1  # 아무것도 선택하지 않았을 때 합이 0이 되는 경우의 수 = 1

    for num in nums:
        print(num, "시작")
        for i in range(target, num - 1, -1):
            dp[i] += dp[i - num]
            print(dp[i])

    return dp[target]


# 테스트 코드
def test_count_subset_sum():
    tests = [
        {"index": 1, "nums": [1, 2, 3], "target": 4, "want": 1},  # 1+3
        {"index": 2, "nums": [2, 4, 6, 10], "target": 16, "want": 2},  # 6+10, 2+4+10
        {"index": 3, "nums": [1, 1, 1, 1], "target": 2, "want": 6},  # (1,1) 조합 6개
        {"index": 4, "nums": [5, 10, 12, 13, 15, 18], "target": 30, "want": 3},
        {"index": 5, "nums": [3, 34, 4, 12, 5, 2], "target": 9, "want": 3},
    ]

    for t in tests:
        got = count_subset_sum(t["nums"], t["target"])
        if got != t["want"]:
            print(
                f"❌ 실패: 테스트 {t['index']} - count_subset_sum({t['nums']}, {t['target']}) = {got}; expected {t['want']}")
        else:
            print(f"✅ 성공: 테스트 {t['index']} - got = {got}")


# 테스트 실행
test_count_subset_sum()
