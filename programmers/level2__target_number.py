# https://programmers.co.kr/learn/courses/30/lessons/43165
# 타겟 넘버, level 2

num = list()
last_stage = 0
key = 0
ways = 0


def dfs(stage: int, value: int):
    global ways

    if stage == last_stage:
        print(value)
        if value == key:
            ways += 1
        return

    pv = value + num[stage]
    dfs(stage+1, pv)
    mv = value - num[stage]
    dfs(stage+1, mv)


def solution(numbers, target):
    global num, last_stage, key

    num = numbers
    last_stage = len(num)
    key = target

    dfs(0, 0)
    return ways


numbers = [1, 1, 1, 1, 1]
target = 3
print("ways:", solution(numbers, target))
