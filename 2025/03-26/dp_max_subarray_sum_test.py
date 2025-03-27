def max_subarray_sum(nums):
    sums = [0 for _ in nums]  # 각 위치까지의 최대 연속합 저장용
    sums[0] = nums[0]  # 초기값: 첫 원소 자체

    for i in range(1, len(nums)):
        sums[i] = max(nums[i], nums[i] + sums[i - 1])  # 새로 시작 or 이전 누적

    return max(sums)  # 전체 중 최댓값 반환


def max_subarray_sum_better(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


tests = [
    {"index": 1, "nums": [-2, 1, -3, 4, -1, 2, 1, -5, 4], "want": 6},
    {"index": 2, "nums": [1], "want": 1},
    {"index": 3, "nums": [5, 4, -1, 7, 8], "want": 23},
    {"index": 4, "nums": [-1, -2, -3], "want": -1},
    {"index": 5, "nums": [1, -2, 3, 5, -1, 2], "want": 9},
]

for t in tests:
    got = max_subarray_sum_better(t["nums"])
    if got != t["want"]:
        print(f"❌ 실패: 테스트 {t['index']} - max_subarray_sum({t['nums']}) = {got}; expected {t['want']}")
    else:
        print(f"✅ 성공: 테스트 {t['index']} - got = {got}")
