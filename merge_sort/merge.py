def _merge(left, right):
    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)

    holder = [0]*(len(left) + len(right))
    left_index = 0
    right_index = 0
    current_index = 0

    while (left_index < len(left)) and (right_index < len(right)):
        if left[left_index] <= right[right_index]:
            holder[current_index] = left[left_index]
            left_index += 1
        else:
            holder[current_index] = right[right_index]
            right_index += 1
        current_index += 1

    while (left_index < len(left)):
        holder[current_index] = left[left_index]
        left_index += 1
        current_index += 1
    while (right_index < len(right)):
        holder[current_index] = right[right_index]
        right_index += 1
        current_index += 1

    return holder


def _merge2(left, right):
    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)

    NL, NR = len(left), len(right)
    holder = [0] * (NL + NR)
    left_index, right_index = 0, 0
    current_index = 0
    while (left_index < NL) and (right_index < NR):
        if left[left_index] <= right[right_index]:
            holder[current_index] = left[left_index]
            left_index += 1
        else:
            holder[current_index] = right[right_index]
            right_index += 1
        current_index += 1

    if (left_index < NL):
        holder[current_index:] = left[left_index:]
    if (right_index < NR):
        holder[current_index:] = right[right_index:]
    return holder

def merge_sort(L):
    split = len(L) // 2
    return _merge(L[:split], L[split:])


if __name__ == '__main__':
    import time
    import random
    random.seed(42)
    L = [random.random() for _ in range(100000)]
    start = time.time()
    S = merge_sort(L)
    end = time.time()

    print(f"Took {end-start} seconds")

