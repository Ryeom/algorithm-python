"""
🧩 문제: 나무 자르기
🧾 설명
농부 상근이는 나무 M미터가 필요하다.
그는 나무를 자를 수 있는 절단기를 가지고 있다.
절단기는 높이 H로 설정되며, 나무를 H보다 높게 자르면 초과 부분이 잘려나간다.

상근이는 절단기 높이를 설정하여 필요한 만큼만 나무를 가져가려 한다.
절단기의 높이를 최대한 높게 설정했을 때 그 높이를 구하라.

잘린 나무 = 각 나무의 남은 부분이 아닌 절단기보다 높아서 잘려나간 윗부분

절단기 높이를 최대한 높게(H) 설정하고,
그렇게 잘린 나무들의 합이 최소 m 이상이 되게 하라

🔢 입력
trees: 나무의 높이 리스트 (예: [20, 15, 10, 17])
m: 필요한 총 나무 길이 (예: 7)

"""


def max_saw_height(trees, m):
    left = 0
    right = max(trees)
    answer = 0

    def is_ok(trees, m, h):
        total = 0
        for tree in trees:
            if tree > h:
                total += (tree - h)

        return total >= m

    while left <= right:
        mid = (left + right) // 2
        if is_ok(trees, m, mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer  # 임시값


def test_max_saw_height():
    tests = [
        {
            "index": 1,
            "trees": [20, 15, 10, 17],
            "m": 7,
            "want": 15
        },
        {
            "index": 2,
            "trees": [4, 42, 40, 26, 46],
            "m": 20,
            "want": 36
        },
        {
            "index": 3,
            "trees": [5, 5, 5, 5],
            "m": 6,
            "want": 3
        }
    ]

    for tt in tests:
        got = max_saw_height(tt["trees"], tt["m"])
        if got != tt["want"]:
            print(f"❌ 실패: 테스트 {tt['index']} - got {got}, expected {tt['want']}")
        else:
            print(f"✅ 성공: 테스트 {tt['index']} - got {got}")

test_max_saw_height()