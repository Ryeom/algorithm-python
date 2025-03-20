def min_coins(coins, amount):
    if amount ==0 :
        return 0

    coins = sorted(coins, reverse=True) # 큰 동전 부터
    ret = 0

    for c in coins :
        n = amount//c
        amount -= c*n
        ret +=n

    return ret if amount ==0 else -1

# 테스트 코드
def test_min_coins():
    # 예시 테스트 케이스
    coins = [1, 2, 5]
    amount = 11
    result = min_coins(coins, amount)
    assert result == 3, f"Expected 3, but got {result}"

    coins = [2]
    amount = 3
    result = min_coins(coins, amount)
    assert result == -1, f"Expected -1, but got {result}"

    coins = [1]
    amount = 0
    result = min_coins(coins, amount)
    assert result == 0, f"Expected 0, but got {result}"

    print("모든 테스트 케이스가 통과했습니다!")

# 테스트 실행
test_min_coins()
