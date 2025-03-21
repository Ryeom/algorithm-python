import heapq


def min_water_supply(n, pipes): # 크루스칼
    pipes = sorted(pipes, key=lambda x: x[2])  # 길이 짧은 순으로 오름차순
    print("파이프",pipes)
    parent = [i for i in range(n + 1)]
    print("부모", parent)

    def find(x):  # x의 최상위 부모 (대표)찾기
        print("파인드", x, parent[x] != x)
        if parent[x] != x:
            parent[x] = find(parent[x])  # 재귀로 루트 갱신
            print("root 갱신함", x, parent[x])

        print("부모현황",parent)
        return parent[x]

    def union(x, y):  # x,y를 하나의 집합으로 병합 (서로 다른 집합일 경우에만)
        print("union 함수 시작", x, y)
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x  # y의 루트를 x의 루트로 병합
            return True  # 병합 성공
        return False  # 이미 같은 집합이면 병합하지 않음

    total_cost = 0
    connected = 0  # 연결된 선의 수 (n개의 집이면 n-1연결이 필요하다)
    for a, b, cost in pipes:
        if union(a, b):
            total_cost += cost
            connected += 1
            if connected == n - 1:
                break

    print(n, "부모입니다. ", parent)
    print(find(2))
    # for house1, house2, length in pipes:

    return total_cost  # 임시값


# ✅ 테스트 코드 (학습 날짜: YYYY-MM-DD)
def test_min_water_supply():
    tests = [
        {"index": 1, "n": 3, "pipes": [(1, 2, 1), (2, 3, 2), (1, 3, 2)], "want": 3},
        {"index": 2, "n": 4, "pipes": [(1, 2, 5), (1, 3, 10), (2, 3, 4), (3, 4, 3)], "want": 12},
        {"index": 3, "n": 5, "pipes": [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6), (1, 5, 15)], "want": 18},
        {"index": 4, "n": 6, "pipes": [(1, 2, 2), (2, 3, 3), (3, 4, 1), (4, 5, 4), (5, 6, 2), (1, 6, 10)], "want": 12},
        {"index": 5, "n": 7, "pipes": [(1, 2, 1), (2, 3, 2), (3, 4, 3), (4, 5, 4), (5, 6, 5), (6, 7, 6), (1, 7, 20)],
         "want": 21},
    ]

    for test in tests:
        got = min_water_supply(test["n"], test["pipes"])
        if got != test["want"]:
            print(f"❌ 실패: 테스트 {test['index']} - got {got}, expected {test['want']}")
        else:
            print(f"✅ 성공: 테스트 {test['index']} - got {got}")


# ✅ 테스트 실행
test_min_water_supply()
