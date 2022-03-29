
from sorting_algos import bubble_sort,merge_sort,selection_sort,quick_sort,insertion_sort
import time
import random

random_lst = []

no_of_ints = int(input("Enter the length of the list: "))

range_of_list = int(input("Enter the range of the list: "))

for i in range(no_of_ints):
    random_lst.append(random.randint(0,range_of_list))

# print(random_lst)
# print(len(random_lst))

no_of_runs = int(input("Enter the number of runs: "))

print("\n")
if no_of_runs < 0:
    print("Negative Numbers are not allowed")
elif no_of_runs == 0:
    print("No runs initiated !!")
else:
    for i in range(1,no_of_runs+1):
        print(f"Run number: {i}")
        bubble_sort_time_start = time.time()
        bubble_sort(random_lst)
        bubble_sort_time_stop = time.time()
        print(f"Bubble sort       -> Elapsed Time: {bubble_sort_time_stop -   bubble_sort_time_start} seconds")


        selection_sort_time_start = time.time()
        selection_sort(random_lst)
        selection_sort_time_stop = time.time()
        print(f"Selection sort    -> Elapsed Time: {selection_sort_time_stop - selection_sort_time_start}seconds")


        insertion_sort_time_start = time.time()
        insertion_sort(random_lst)
        insertion_sort_time_stop = time.time()
        print(f"Insertion sort    -> Elapsed Time: {insertion_sort_time_stop - insertion_sort_time_start} seconds")

        quick_sort_time_start = time.time()
        quick_sort(random_lst)
        quick_sort_time_stop = time.time()
        print(f"Quick sort        -> Elapsed Time: {quick_sort_time_stop - quick_sort_time_start} seconds")


        merge_sort_time_start = time.time()
        merge_sort(random_lst)
        merge_sort_time_stop = time.time()
        print(f"Merge sort        -> Elapsed Time: {merge_sort_time_stop - merge_sort_time_start} seconds")

        built_in_sort_start = time.time()
        random_lst.sort()
        built_in_sort_stop = time.time()
        print(f"Built in sort     -> Elapsed Time: {built_in_sort_stop - built_in_sort_start} seconds")
        print("-----------------------------------------------------")
        print("\n")

