# 内包表記の練習

sample_list = [x for x in range(5)]
print(sample_list)  # '[0, 1, 2, 3, 4]'と出力


# ランダムの動作チェック
import random

print(random.random())


# 通常のリストの書き方
def random_list(number):
    sample_list2 = [0] * number
    for i in range(0, number):
        sample_list2[i] = random.randint(1, 9)
    print(sample_list2)


random_list(4)

# 内包表記練習
def random_list2(number):
    sample_list2 = [random.randint(1, 9) for i in range(0, number)]
    print(sample_list2)


random_list2(4)


# 同練習2
def create_list(number):
    sample_list2 = [i * 3 for i in range(0, number)]
    print(sample_list2)


create_list(6)

# 同練習3 with if文
def create_list2(number):
    sample_list2 = [
        i * 4 if i % 3 != 0 or i == 0 else "3の倍数です" for i in range(0, number)
    ]
    print(sample_list2)


create_list2(50)
