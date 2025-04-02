def max_non_adjacent_sum(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])  # 첫번쩨가 큰지 두번째가 큰지

    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp[-1]


def test_max_non_adjacent_sum():
    tests = [
        {
            "index": 1,
            "nums": [3, 2, 5, 10, 7],
            "want": 15
        },
        {
            "index": 2,
            "nums": [3, 2, 7, 10],
            "want": 13
        },
        {
            "index": 3,
            "nums": [3, 5, 1, 7, 8, 9],
            "want": 21
        },
        {
            "index": 4,
            "nums": [5, 1, 1, 5],
            "want": 10
        },
    ]

    for t in tests:
        got = max_non_adjacent_sum(t["nums"])
        if got != t["want"]:
            print(f"❌ 실패: 테스트 {t['index']} - got = {got}; expected = {t['want']}")
        else:
            print(f"✅ 성공: 테스트 {t['index']} - got = {got}")


test_max_non_adjacent_sum()
