import time
import random
from bubblesort import bubble_sort
from insertsort import insert_sort
from mergesort import merge_sort
from quicksort import quick_sort
from heapsort import heap_sort

lista = [random.randint(-50, 100) for i in range(10)]

# Zwracane elementy przez poniższe funkcje nie są przechwytywane.
# Są one uruchamiane tylko aby przeliczyć czas działania danej funkcji.

czas0 = time.time()
bubble_sort(lista)
czas1 = time.time()
insert_sort(lista)
czas2 = time.time()
merge_sort(lista)
czas3 = time.time()
quick_sort(lista)
czas4 = time.time()
heap_sort(lista)
czas5 = time.time()
lista.sort()
czas6 = time.time()

print()
print("              typ              │      czas [ms]      ")
print("───────────────────────────────┼─────────────────────");
print("  Sortowanie bąbelkowe         │  {:.15f}".format(czas1 - czas0));
print("  Sortowanie prze wstawianie   │  {:.15f}".format(czas2 - czas1));
print("  Sortowanie przez scalenie    │  {:.15f}".format(czas3 - czas2));
print("  Sortowanie szybkie           │  {:.15f}".format(czas4 - czas3));
print("  Sortowanie przez kopcowanie  │  {:.15f}".format(czas5 - czas4));
print("  Sortowanie TIM (wbudowane)   │  {:.15f}".format(czas6 - czas5));
print()
