def max_subarray_sum(nums):
    # TODO: 여기에 코드를 작성하세요.
    return 0  # 임시값
# 파일명: dp_max_subarray_sum_test.py
# 학습 날짜: 2025-03-24


tests = [
    {"index": 1, "nums": [-2, 1, -3, 4, -1, 2, 1, -5, 4], "want": 6},
    {"index": 2, "nums": [1], "want": 1},
    {"index": 3, "nums": [5, 4, -1, 7, 8], "want": 23},
    {"index": 4, "nums": [-1, -2, -3], "want": -1},
    {"index": 5, "nums": [1, -2, 3, 5, -1, 2], "want": 9},
]

for t in tests:
    got = max_subarray_sum(t["nums"])
    if got != t["want"]:
        print(f"❌ 실패: 테스트 {t['index']} - max_subarray_sum({t['nums']}) = {got}; expected {t['want']}")
    else:
        print(f"✅ 성공: 테스트 {t['index']} - got = {got}")
