"""
DP 문제: 1로 만들기
정수 n이 주어졌을 때, 다음 연산을 활용해서 1로 만들려고 한다.
최소 연산 횟수를 구하시오.

n이 3으로 나누어 떨어지면, 3으로 나눈다.
n이 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.

"""


def make_one(n):
    dp = [0] * (n + 1)  # dp[i] = i를 1로 만드는 최소 연산 수
    dp[1] = 0  # 1은 0번의 연산으로 이미 1
    print(n)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1  # 기본: 1을 빼는 연산
        print (dp[i],i % 2 == 0,i % 3 == 0)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return dp[n]


def test_make_one():
    tests = [
        {"index": 1, "n": 1, "want": 0},
        {"index": 2, "n": 2, "want": 1},
        {"index": 3, "n": 10, "want": 3},
        {"index": 4, "n": 26, "want": 3},
        {"index": 5, "n": 100, "want": 7},
    ]

    for tt in tests:
        got = make_one(tt["n"])
        if got != tt["want"]:
            print(f"❌ 실패: 테스트 {tt['index']} - make_one({tt['n']}) = {got}; expected {tt['want']}")
        else:
            print(f"✅ 성공: 테스트 {tt['index']} - got = {got}")


test_make_one()
