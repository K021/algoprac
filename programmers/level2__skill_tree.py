# https://programmers.co.kr/learn/courses/30/lessons/49993
# 프로그래머스 스킬트리, level 2

def solution(skill, skill_trees):
    order = dict()
    possible_trees_count = len(skill_trees)
    for i, s in enumerate(skill):
        order[s] = i
    for tree in skill_trees:
        i = 0
        former_order = -1
        while i < len(tree):
            if tree[i] not in order:
                i += 1
                continue
            print(f"tree: {tree}, former_order: {former_order}, order[tree[i]]: {order[tree[i]]}")
            if former_order + 1 != order[tree[i]]:
                print(tree)
                possible_trees_count -= 1
                break
            former_order = order[tree[i]]
            i += 1
    return possible_trees_count


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))


# version 2
def solution(order, skill_trees):
    order_set = set(order)
    count = 0
    for tr in skill_trees:
        skills_with_order = [sk for sk in tr if sk in order_set]
        if not skills_with_order:
            count += 1
        elif order.startswith(''.join(skills_with_order)):
            count += 1
    return count
