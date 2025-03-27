"""
🧗 계단 오르기 - 점수 최댓값
📄 문제 설명
총 n개의 계단이 있고, 각 계단에는 정수 점수가 적혀 있음.
한 번에 1칸 또는 2칸씩만 오를 수 있고, 3칸 연속으로는 밟을 수 없음.

또한, 마지막 계단은 반드시 밟아야 함.

제한 조건을 지키면서 얻을 수 있는 최대 점수를 구하시오.

"""


def max_stair_score(stairs):
    n = len(stairs)
    if n == 0:
        return 0
    if n == 1:
        return stairs[0]
    if n == 2:
        return stairs[0] + stairs[1]

    dp = [0] * n  # i 번째 계단까지 최대 점수 저장
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, n):
        dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])
        # dp[i - 2] + stairs[i] : 한칸 건너뛰고 올라옴
        # dp[i - 3] + stairs[i - 1] + stairs[i] : 두 칸 전에서 한칸, 한칸 올라옴
    return dp[-1]



def test_max_stair_score():
    tests = [
        {"index": 1, "stairs": [10, 20, 15, 25, 10, 20], "want": 75},
        {"index": 2, "stairs": [5, 10, 20], "want": 25},
        {"index": 3, "stairs": [30, 10, 20, 15, 10, 20, 25], "want": 90},
        {"index": 4, "stairs": [100], "want": 100},
        {"index": 5, "stairs": [10, 20], "want": 30},
    ]

    for t in tests:
        got = max_stair_score(t["stairs"])
        if got != t["want"]:
            print(f"❌ 실패: 테스트 {t['index']} - max_stair_score({t['stairs']}) = {got}; expected {t['want']}")
        else:
            print(f"✅ 성공: 테스트 {t['index']} - got = {got}")


test_max_stair_score()
