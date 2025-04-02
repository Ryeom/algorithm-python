def can_make_target(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True  # 합이 0이 되는 경우는 "아무것도 선택하지 않은 경우" 항상 존재

    for num in nums:
        for i in range(target, num - 1, -1):
            if dp[i - num]:
                dp[i] = True

    return dp[target]


def can_make_target_dfs(nums, target):
    n = len(nums)
    result = False  # 한 번이라도 성공하면 True

    def dfs(index, total):
        nonlocal result
        if total == target:
            result = True
            return
        if index >= n or total > target:
            return

        # 현재 원소 선택
        dfs(index + 1, total + nums[index])
        # 현재 원소 선택하지 않음
        dfs(index + 1, total)

    dfs(0, 0)
    return result


def test_subset_sum():
    tests = [
        {"index": 1, "nums": [3, 34, 4, 12, 5, 2], "target": 9, "want": True},
        {"index": 2, "nums": [1, 2, 3], "target": 7, "want": False},
        {"index": 3, "nums": [1, 2, 5], "target": 4, "want": False},
        {"index": 4, "nums": [2, 4, 6, 10], "target": 16, "want": True},
        {"index": 5, "nums": [1, 1, 1, 1, 1], "target": 3, "want": True},
    ]

    for t in tests:
        got = can_make_target_dfs(t["nums"], t["target"])
        if got != t["want"]:
            print(f"❌ 실패: 테스트 {t['index']} - can_make_target({t['nums']}, {t['target']}) = {got}; expected {t['want']}")
        else:
            print(f"✅ 성공: 테스트 {t['index']} - got = {got}")


test_subset_sum()