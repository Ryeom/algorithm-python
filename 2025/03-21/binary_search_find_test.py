# 파일명: binary_search_find_test.py

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1  # 임시값


# ✅ 테스트 코드 (학습 날짜: 2025-03-20)
def test_binary_search():
    tests = [
        {"index": 1, "nums": [1, 3, 5, 7, 9], "target": 5, "want": 2},
        {"index": 2, "nums": [1, 3, 5, 7, 9], "target": 6, "want": -1},
        {"index": 3, "nums": [1], "target": 1, "want": 0},
        {"index": 4, "nums": [1], "target": 2, "want": -1},
        {"index": 5, "nums": [2, 4, 6, 8, 10, 12, 14], "target": 14, "want": 6},
    ]

    for test in tests:
        got = binary_search(test["nums"], test["target"])
        if got != test["want"]:
            print(f"❌ 실패: 테스트 {test['index']} - got {got}, expected {test['want']}")
        else:
            print(f"✅ 성공: 테스트 {test['index']} - got {got}")


# ✅ 테스트 실행
test_binary_search()
