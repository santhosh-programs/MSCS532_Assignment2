
import merge_sort
import time
import random


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


arr = [38, 27, 43, 3, 9, 82, 10]
arr2 = [38, 27, 43, 3, 9, 82, 10, 34, 12, 56, 1, 25, 76]


print("Quick sort"+str(quick_sort(arr)))
merge_sort.merge_sort(arr2)
print("Merge sort: "+str(arr2))


def compare(arr):
    arr_merge = arr.copy()
    arr_quick = arr.copy()

    start_time = time.time()
    merge_sort.merge_sort(arr_merge)
    merge_sort_time = time.time() - start_time

    start_time = time.time()
    quick_sort(arr_quick)
    quick_sort_time = time.time() - start_time

    return merge_sort_time, quick_sort_time


sorted_data = list(range(10000))
reverse = sorted_data[::-1]
random = random.sample(range(10000), 10000)

sorted_r = compare(sorted_data)
reverse_r = compare(reverse)
random_r = compare(random)

print(sorted_r, reverse_r, random_r)
