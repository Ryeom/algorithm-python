def min_cost_to_connect_islands(n, bridges):
    bridges.sort(key=lambda x: x[2])
    parent = [i for i in range(n + 1)]

    def find(p, x):
        if p[x] != x:
            p[x] = find(p, p[x])
        return p[x]

    def union(p, x, y):
        root_x = find(p, x)
        root_y = find(p, y)
        if root_x < root_y:
            p[root_y] = root_x
        else:
            p[root_x] = root_y

    min_cost = 0
    for node1, node2, cost in bridges:
        if find(parent, node1) != find(parent, node2):
            union(parent, node1, node2)
            min_cost += cost

    return min_cost



def test_min_cost_to_connect_islands():
    tests = [
        {"index": 1, "n": 4, "bridges": [(1, 2, 1), (2, 3, 2), (3, 4, 3), (1, 4, 100)], "want": 6},
        {"index": 2, "n": 3, "bridges": [(1, 2, 10), (2, 3, 15), (1, 3, 5)], "want": 15},
        {"index": 3, "n": 5, "bridges": [(1, 2, 2), (1, 3, 3), (3, 4, 4), (4, 5, 5), (2, 5, 10)], "want": 14},
        {"index": 4, "n": 6, "bridges": [(1, 2, 1), (2, 3, 1), (3, 4, 1), (4, 5, 1), (5, 6, 1), (1, 6, 10)], "want": 5},
        {"index": 5, "n": 4, "bridges": [(1, 2, 4), (2, 3, 3), (3, 4, 2), (1, 4, 1)], "want": 6},
    ]

    for test in tests:
        got = min_cost_to_connect_islands(test["n"], test["bridges"])
        if got != test["want"]:
            print(f"❌ 실패: 테스트 {test['index']} - got {got}, expected {test['want']}")
        else:
            print(f"✅ 성공: 테스트 {test['index']} - got {got}")


# ✅ 테스트 실행
test_min_cost_to_connect_islands()
