data = [1, 2, 9, 12, 20, 25, 32, 48, 50, 57, 72, 78, 80, 93]
key = int(input("探す値を入力してください"))
left = 0
right = len(data) - 1
flg = False

while left <= right:
    mid = (left + right) // 2
    # mid_1 = (left + right) / 2
    # print("mid: ", mid, ", mid_1: ", mid_1)
    print("L={} M={} R={}".format(left, mid, right))
    if data[mid] == key:
        print("data[{}]が{}です".format(mid, key))
        flg = True
        break
    if data[mid] < key:
        left = mid + 1
    else:
        right = mid - 1

if flg == False:
    print("その値は見つかりませんでした")
