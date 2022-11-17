from random import randint
from time import time
from collections import deque


class OnlyGetArray:
    def __init__(self, func):
        self.func = func
        self.__name__ = self.func.__name__

    def __call__(self, *args, **kwargs):
        if len(args) == 1:
            arr = args[0]
            if not arr:
                return arr
            return self.func(arr, 0, len(arr) - 1)
        else:
            return self.func(*args, **kwargs)


def quicksort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[len(arr) // 2]
    left = list()
    right = list()
    equals = list()

    for n in arr:
        if n < pivot:
            left.append(n)
        elif n > pivot:
            right.append(n)
        else:
            equals.append(n)

    return quicksort(left) + equals + quicksort(right)


def quicksort2(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[len(arr) // 2]
    left = [i for i in arr if i < pivot]
    mid = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]

    return quicksort2(left) + mid + quicksort2(right)


# @OnlyGetArray  # arr 만 받을 수 있도록 하기 위해 만들었으나, 속도에 영향을 미쳐서 제거하였다
def quicksort_raw(arr, start, end):
    def partition(arr, start, end):
        mid = (start + end) // 2
        arr[start], arr[mid] = arr[mid], arr[start]
        pivot = arr[start]
        left = start + 1
        right = end
        while left <= right:
            # swap 전에 left, right 의 대소관계를 확인해야 하기 때문에 여기서 swap 한다
            arr[left], arr[right] = arr[right], arr[left]
            # left 는 항상 pivot 보다 큰 수에서 멈추고
            # right 은 항상 pivot 보다 작은 수에서 멈춘다
            # 따라서 둘이 같은 곳에서 멈추는 경우는 없고, 만나지 않거나 엇갈리거나 한다
            # 만나지 않으면 swap 하고, 엇갈리면 break 한다
            while left <= right and arr[left] <= pivot:
                left += 1
            while left <= right and arr[right] >= pivot:
                right -= 1
        arr[start], arr[right] = arr[right], arr[start]
        return right

    if start < end:  # 이 조건이 깨지면 len(arr) <= 1
        partition_point = partition(arr, start, end)
        quicksort_raw(arr, start, partition_point - 1)
        quicksort_raw(arr, partition_point + 1, end)

    return arr


def quicksort_mix(arr):
    if len(arr) < 2:
        return arr

    n = len(arr)
    arr[0], arr[n // 2] = arr[n // 2], arr[0]
    pivot = arr[0]
    left = 1
    right = n - 1

    while left <= right:
        arr[left], arr[right] = arr[right], arr[left]
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1

    return quicksort_mix(arr[1:left]) + [pivot] + quicksort_mix(arr[left:])


def mergesort(arr):
    if len(arr) < 2:
        return arr

    h = len(arr) // 2
    a = mergesort(arr[:h])
    b = mergesort(arr[h:])

    merged = list()
    ai, bi = 0, 0
    an, bn = len(a), len(b)
    while ai < an and bi < bn:
        if a[ai] < b[bi]:
            merged.append(a[ai])
            ai += 1
        else:
            merged.append(b[bi])
            bi += 1
    merged.extend(a[ai:])
    merged.extend(b[bi:])

    return merged


def mergesort2(arr):
    if len(arr) < 2:
        return arr

    h = len(arr) // 2
    a = deque(mergesort2(arr[:h]))
    b = deque(mergesort2(arr[h:]))

    merged = list()
    while a and b:
        if a[0] < b[0]:
            merged.append(a.popleft())
        else:
            merged.append(b.popleft())
    merged.extend(a)
    merged.extend(b)

    return merged


def mergesort3(arr):
    if len(arr) < 2:
        return arr

    h = len(arr) // 2
    a = mergesort3(arr[:h])
    b = mergesort3(arr[h:])

    merged = []
    ai, bi = 0, 0
    an, bn = len(a), len(b)
    while ai < an and bi < bn:
        av, bv = a[ai], b[bi]
        if av <= bv:
            merged.append(av)
            ai += 1
        else:
            merged.append(bv)
            bi += 1
    merged.extend(a[ai:])
    merged.extend(b[bi:])

    return merged


def bubblesort(arr):
    n = len(arr)
    for i in range(n - 1):
        for k in range(n - 1 - i):
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]
    return arr


def selectionsort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for k in range(i + 1, n):
            if arr[k] < arr[min_idx]:
                min_idx = k
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def selectionsort2(arr):
    for base in range(len(arr) - 1):
        mini = arr[base]
        minind = base
        for candidate in range(base + 1, len(arr)):
            if arr[candidate] < mini:
                mini = arr[candidate]
                minind = candidate
        arr[base], arr[minind] = arr[minind], arr[base]

    return arr


def insertionsort(arr):
    for right in range(1, len(arr)):
        for left in range(right - 1, -2, -1):
            if left == -1 or arr[left] < arr[right]:
                right_n = arr.pop(right)
                arr.insert(left + 1, right_n)
                break
    return arr


def shellsort(arr):
    def insertionsort(arr, start, gap):
        n = len(arr)
        loop_count = (n - start) // gap
        loop_count += 1 if (n - start) % gap else 0
        for i in range(start + gap, start + loop_count * gap, gap):
            for k in range(i - gap, start - gap - 1, -gap):
                if k == start - gap or arr[i] > arr[k]:
                    ni = arr[i]
                    for ki in range(i - gap, k, -gap):
                        arr[ki + gap] = arr[ki]
                    arr[k + gap] = ni
                    break
        return arr

    gap = len(arr) // 2
    gap += 1 if gap % 2 == 0 else 0
    while gap > 1:
        print("gap:", gap)
        for start in range(gap):
            insertionsort(arr, start, gap)
        gap //= 2
        gap += 1 if gap % 2 == 0 else 0
    insertionsort(arr, 0, 1)
    return arr


def shellsort2(arr):
    def insertionsort(arr, start, gap):
        for right in range(start + gap, len(arr), gap):
            for left in range(right - gap, start - gap - 1, -gap):
                if left == start - gap or arr[left] < arr[right]:
                    right_n = arr[right]
                    for mid in range(right - gap, left, -gap):
                        arr[mid + gap] = arr[mid]
                    arr[left + gap] = right_n
                    break

    gap = len(arr)
    while gap > 1:
        gap //= 2
        gap += 1 if gap % 2 == 0 else 0
        for start in range(gap):
            insertionsort(arr, start, gap)

    return arr


def shellsort_print(arr):
    def insertionsort(arr, start, gap):
        n = len(arr)
        loop_count = (n - start) // gap
        loop_count += 1 if (n - start) % gap else 0
        print(f"loop_count: {loop_count}")
        for i in range(start + gap, start + loop_count * gap, gap):
            print(f"  i: {i}")
            for k in range(i - gap, start - gap - 1, -gap):
                print(f"    k: {k}")
                if k == start - gap or arr[i] > arr[k]:
                    ni = arr[i]
                    for ki in range(i - gap, k, -gap):
                        arr[ki + gap] = arr[ki]
                    arr[k + gap] = ni
                    print("      arr:", arr)
                    break
        return arr

    gap = len(arr) // 2
    gap += 1 if gap % 2 == 0 else 0
    while gap > 1:
        for start in range(gap):
            print("===============================")
            print(f"start: {start}, gap: {gap}")
            print("before:", arr)
            insertionsort(arr, start, gap)
            print("after :", arr)
        gap //= 2
        gap += 1 if gap % 2 == 0 else 0
    insertionsort(arr, 0, 1)
    print(arr)
    return arr


def test_sort(
    sort_func,
    arr_size=100000,
    arr=None,
    random=True,
    end=None,
    print_arr=False,
):
    print(f"<{sort_func.__name__}>")

    unsorted_base = [2, 5, 3, 1, 7, 0, 9, 8, 4, 3, 4, 6, 8, 2] if not arr else arr
    unsorted = (
        [randint(0, arr_size) for _ in range(arr_size)] if random else unsorted_base
    )
    unsorted_copy = unsorted.copy()

    sorted_ = list()
    consumed_time = -1
    if sort_func.__code__.co_argcount == 1:
        start_time = time()
        sorted_ = sort_func(unsorted_copy)
        consumed_time = time() - start_time
    elif sort_func.__code__.co_argcount == 3:
        start_time = time()
        sorted_ = sort_func(unsorted_copy, 0, len(unsorted_copy) - 1)
        consumed_time = time() - start_time
    if print_arr:
        print("origin: ", unsorted[:30])
        print("result: ", sorted_[:30])
    print(
        "consumed time: ",
        consumed_time,
        f"s ({arr_size if random else len(unsorted_base)} elements)",
    )

    cntdic = dict()
    for n in unsorted:
        if n not in cntdic:
            cntdic[n] = 1
        else:
            cntdic[n] += 1
    for n in sorted_:
        if n not in cntdic:
            cntdic[n] = -1
        else:
            cntdic[n] -= 1
    is_element_changed = False
    for v in cntdic.values():
        if v != 0:
            is_element_changed = True
            break
    print("elements conservation: ", not is_element_changed)

    is_sorted = True
    for former, latter in zip(sorted_, sorted_[1:]):
        if former > latter:
            is_sorted = False
            break
    print("sorted: ", is_sorted)

    if end:
        print(end=end)


# arr = [10, 8, 6, 20, 15, 3, 22, 1, 0, 4, 16]
# test_sort(mergesort_test, arr=arr, random=False, end='\n', print_arr=False)
# test_sort(shellsort, arr_size=10000, random=True, end="\n", print_arr=False)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", help="sort function name", type=str)

    args = parser.parse_args()

    sorting_func = globals().get(args.name)
    if not sorting_func:
        print(f"invalid function name: {args.name}")

    test_sort(sorting_func, arr_size=10000, random=True, end="\n", print_arr=False)


## 성능 평가 결과 ##
# <sorted> (내장함수, c 로 짜여진 거라 훨씬 빠르다. timsort 로 구현되어 있다)
# consumed time:  0.01555490493774414 s (100000 elements)
# elements conservation:  True
# sorted:  True
#
# <quicksort>
# consumed time:  0.011842012405395508 s (10000 elements)
# elements conservation:  True
# sorted:  True
#
# <quicksort2>
# consumed time:  0.018123149871826172 s (10000 elements)
# elements conservation:  True
# sorted:  True
#
# <quicksort_raw>
# consumed time:  0.014657020568847656 s (10000 elements)
# elements conservation:  True
# sorted:  True
#
# <mergesort>
# consumed time:  0.017892122268676758 s (10000 elements)
# elements conservation:  True
# sorted:  True
#
# <mergesort2>
# consumed time:  0.026575803756713867 s (10000 elements)
# elements conservation:  True
# sorted:  True
# 
# <mergesort3>
# consumed time:  0.016479969024658203 s (10000 elements)
# elements conservation:  True
# sorted:  True
#
# <bubblesort>
# consumed time:  4.338186979293823 s (10000 elements)
# elements conservation:  True
# sorted:  True
#
# <selectionsort>
# consumed time:  1.9003660678863525 s (10000 elements)
# elements conservation:  True
# sorted:  True
#
# <selectionsort2>
# consumed time:  1.7047178745269775 s (10000 elements)
# elements conservation:  True
# sorted:  True
#
# <insertionsort>
# consumed time:  1.1842241287231445 s (10000 elements)
# elements conservation:  True
# sorted:  True
#
# <shellsort>
# consumed time:  0.09445810317993164 s (10000 elements)
# elements conservation:  True
# sorted:  True
#
# <shellsort2>
# consumed time:  0.09250998497009277 s (10000 elements)
# elements conservation:  True
# sorted:  True
#
