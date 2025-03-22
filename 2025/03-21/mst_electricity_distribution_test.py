"""
📝 문제 설명
N개의 도시가 있다. 이 도시들은 전선을 통해 전력을 서로 공급할 수 있다.
도시 사이에 전선을 연결하는 데에는 비용이 들고, 일부 도시에는 자체 발전소가 있어 전기를 공급할 수 있다.

모든 도시는 전력을 받아야 하며,
각 도시는 다음 두 가지 방법 중 하나로 전기를 공급받을 수 있다:

자체 발전소 사용 (비용 있음)
다른 도시와 전선으로 연결 (연결된 도시는 전기를 공유함)
모든 도시에 전기가 공급되도록 할 때, 필요한 최소 비용을 구하라.
"""


def min_electricity_cost(n, plants, connections):  # plants : i번 도시에 발전소를 지을 경우의 비용
    city = [i for i in range(n + 1)]

    self = []
    for i, cost in enumerate(plants):  # 자체 발전소를 간선으로 추가
        self.append((0, i + 1, cost))

    connections = [*connections, *self]

    connections.sort(key=lambda x: (x[2], -1 if x[0] == 0 or x[1] == 0 else 1))

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

    result_cost = 0
    edge_count = 0
    for node1, node2, cost in connections:
        if find(city, node1) != find(city, node2):
            union(city, node1, node2)
            result_cost += cost
            edge_count += 1
            if edge_count == n:
                break

    return result_cost


def test_min_electricity_cost():
    # connections : 도시, 도시, 비용
    tests = [
        {
            "index": 1,
            "n": 4,
            "plants": [1, 2, 3, 4],
            "connections": [
                (1, 2, 1),
                (2, 3, 1),
                (3, 4, 1),
                (1, 4, 100)
            ],
            "want": 4  # 발전소 1 + 연결 3 = 4
        },
        {
            "index": 2,
            "n": 3,
            "plants": [10, 1, 10],
            "connections": [
                (1, 2, 100),
                (2, 3, 100)
            ],
            "want": 21  # 발전소 2 + 연결 1*1 = 21
        },
        {
            "index": 3,
            "n": 2,
            "plants": [5, 5],
            "connections": [
                (1, 2, 1)
            ],
            "want": 6  # 발전소 5 + 연결 1
        },
        {
            "index": 4,
            "n": 5,
            "plants": [1, 1, 1, 1, 1],
            "connections": [],
            "want": 5  # 발전소만 5개 설치 (연결 없음)
        },
        {
            "index": 5,
            "n": 3,
            "plants": [10, 10, 1],
            "connections": [
                (1, 2, 2),
                (2, 3, 2)
            ],
            "want": 5  # 발전소 1 + 연결 2 + 2
        }
    ]
    for test in tests:
        got = min_electricity_cost(test["n"], test["plants"], test["connections"])
        if got != test["want"]:
            print(f"❌ 실패: 테스트 {test['index']} - got {got}, expected {test['want']}")
        else:
            print(f"✅ 성공: 테스트 {test['index']} - got {got}")


# ✅ 테스트 실행
test_min_electricity_cost()
