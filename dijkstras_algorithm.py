F = 99999
way = [
    [F, 3, 2, 5, F, F, F],
    [3, F, F, F, 7, F, F],
    [2, F, F, 2, F, 4, F],
    [5, F, 2, F, F, 1, F],
    [F, F, F, F, F, 4, 5],
    [F, F, 4, 1, 4, F, 3],
    [F, F, F, F, 5, 3, F],
]
# 経路の個数取得
len = len(way)

# 初期配列変数の初期設定
dist = [F] * len
flg = [0] * len
route = [-1] * len

# スタート地点を設定
start = 5
p = start
dist[p] = 0
print("地点", p)


for i in range(len):
    d = F
    for j in range(len):
        if flg[j] == 0 and dist[j] < d:
            p = j
            d = dist[j]
    flg[p] = 1
    for k in range(len):
        if dist[p] + way[p][k] < dist[k]:
            dist[k] = dist[p] + way[p][k]
            route[k] = p

print("各ノードまでの距離")
for i in range(7):
    print("ノード{}まで{}".format(i, dist[i]))

print("routeの値", route)
e = int(input("道順を示す終点ノードの番号は？"))
while route[e] >= 0:
    print(e, end="←")
    e = route[e]
print(start)
