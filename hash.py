HASH = 5
names = [None] * HASH
tels = [None] * HASH


def hash(key):
    h = 0
    for i in key:
        h = h + ord(i)
    return h % HASH


def open_add(name, tel, hash_number):
    flg = False
    for i in range(HASH - 1):
        hash_number = (hash_number + 1) % HASH
        if names[hash_number] == None:
            names[hash_number] = name
            tels[hash_number] = tel
            flg = True
            print("再ハッシュ", hash_number, "データ格納完了")
            break
    if flg == False:
        print("データを格納できる領域がありません")


def search_rehash(key, hash_number):
    for i in range(HASH - 1):
        hash_number = (hash_number + 1) % HASH
        if names[hash_number] == key:
            return hash_number
    return -1


while True:
    name = input("名前を入力してください")
    if name == "":
        break
    tel = input("電話番号を入力してください")
    hash_number = hash(name)
    if names[hash_number] == None:
        names[hash_number] = name
        tels[hash_number] = tel
        print("ハッシュ値", hash_number, "データ格納完了")
    else:
        open_add(name, tel, hash_number)

print(names)
print(tels)

while True:
    name = input("検索する名前は？ ")
    if name == "":
        break
    hash_number = hash(name)
    if names[hash_number] == name:
        print(name + "さんの番号は" + tels[hash_number])
    elif names[hash_number] == "None":
        print("その名前は登録されていません")
    else:
        hash_number = search_rehash(name, hash_number)
        if hash_number == -1:
            print("その名前は登録されていません")
        else:
            print(name + "さんの番号は" + tels[hash_number])
