def max_triangle_path_(triangle):
    n = len(triangle)
    temp = [[0 for _ in row] for row in triangle]
    temp[0][0] = triangle[0][0]
    print(temp)
    for i in range(1, n):
        for j in range(len(triangle[i])):
            # 왼쪽 끝
            if j == 0:
                temp[i][j] = temp[i - 1][j] + triangle[i][j]
            # 오른쪽 끝
            elif j == len(triangle[i]) - 1:
                temp[i][j] = temp[i - 1][j - 1] + triangle[i][j]
            # 중간
            else:
                temp[i][j] = max(temp[i - 1][j - 1], temp[i - 1][j]) + triangle[i][j]

    return max(temp[-1])


def max_triangle_path(triangle):
    n = len(triangle)
    temp = [[0] * len(row) for row in triangle]
    temp[0][0] = triangle[0][0]

    for i in range(1, n):
        for j in range(len(triangle[i])):
            # 왼쪽 끝
            if j == 0:
                temp[i][j] = temp[i-1][j] + triangle[i][j]
            # 오른쪽 끝
            elif j == len(triangle[i]) - 1:
                temp[i][j] = temp[i-1][j-1] + triangle[i][j]
            # 중간
            else:
                temp[i][j] = max(temp[i-1][j-1], temp[i-1][j]) + triangle[i][j]

    return max(temp[-1])



def test_max_triangle_path():
    tests = [
        {
            "index": 1,
            "triangle": [
                [7],
                [3, 8],
                [8, 1, 0],
                [2, 7, 4, 4],
                [4, 5, 2, 6, 5]
            ],
            "want": 30
        },
        {
            "index": 2,
            "triangle": [
                [1],
                [2, 3],
                [4, 5, 6]
            ],
            "want": 10
        },
        {
            "index": 3,
            "triangle": [
                [5]
            ],
            "want": 5
        },
    ]

    for t in tests:
        got = max_triangle_path(t["triangle"])
        if got != t["want"]:
            print(f"❌ 실패: 테스트 {t['index']} - max_triangle_path({t['triangle']}) = {got}; expected {t['want']}")
        else:
            print(f"✅ 성공: 테스트 {t['index']} - got = {got}")


test_max_triangle_path()
