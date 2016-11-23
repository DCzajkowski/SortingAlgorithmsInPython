import random
from bubblesort import bubble_sort
from insertsort import insert_sort
from mergesort import merge_sort
from quicksort import quick_sort
from heapsort import heap_sort

random_items = [random.randint(-50, 100) for c in range(1000)]
# random_items = [-44, -33, 75, 94, 91, 61, 21, -8, -15, -36]

print('Before:', random_items)
# random_items = bubble_sort(random_items)
# random_items = insert_sort(random_items)
# random_items = merge_sort(random_items)
random_items = quick_sort(random_items)
# random_items = heap_sort(random_items)
print('After:', random_items)
