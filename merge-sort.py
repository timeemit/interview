import random

# O(n) = n * log(n)  # => Average & worst case

global call_count
call_count = 0

def mergesort(array):
    global call_count

    if len(array) == 1:
        return array

    mid = len(array) // 2  # 9 // 2 ==> 4

    # Map / Split
    left = mergesort(array[:mid])
    right = mergesort(array[mid:])

    # Merge / Reduce
    merge = list()
    left_i, right_i = 0, 0
    while left_i < len(left) and right_i < len(right):
        call_count += 1
        l, r = left[left_i], right[right_i]
        if l <= r:
            merge.append(l)
            left_i += 1
        else:
            merge.append(r)
            right_i += 1

    # Catch left overs
    if left_i < len(left):
        merge.extend(left[left_i:])
    if right_i < len(right):
        merge.extend(right[right_i:])

    return merge


if __name__ == "__main__":
    a = list(range(10))
    random.shuffle(a)
    print(a)
    a = mergesort(a)
    print(a)
    print(call_count)
