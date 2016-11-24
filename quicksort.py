def quick_sort(items):
    if len(items) > 1:
        pivot_index = int(len(items) / 2)
        smaller = []
        larger = []

        for i, item in enumerate(items):
            if i != pivot_index:
                if item < items[pivot_index]:
                    smaller.append(item)
                else:
                    larger.append(item)

        quick_sort(smaller)
        quick_sort(larger)

        items[:] = smaller + [items[pivot_index]] + larger

    return items
