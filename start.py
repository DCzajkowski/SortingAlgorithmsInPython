import time
import random
from bubblesort import bubble_sort
from insertsort import insert_sort
from mergesort import merge_sort
from quicksort import quick_sort
from heapsort import heap_sort

items = [random.randint(-50, 100) for i in range(10)]

time0 = time.time()
bubble_sort(items)
time1 = time.time()
insert_sort(items)
time2 = time.time()
merge_sort(items)
time3 = time.time()
quick_sort(items)
time4 = time.time()
heap_sort(items)
time5 = time.time()
items.sort()
time6 = time.time()

print()
print("         typ         │      time [ms]      ")
print("─────────────────────┼─────────────────────");
print("  Bubble sort        │  {:.15f}".format(time1 - time0));
print("  Insertion sort     │  {:.15f}".format(time2 - time1));
print("  Merge sort         │  {:.15f}".format(time3 - time2));
print("  Quicksort          │  {:.15f}".format(time4 - time3));
print("  Heapsort           │  {:.15f}".format(time5 - time4));
print("  Timsort            │  {:.15f}".format(time6 - time5));
print()
