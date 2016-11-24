def merge_sort(items):
    if len(items) > 1:
        mid = int(len(items) / 2)
        left = items[0:mid]
        right = items[mid:]

        merge_sort(left)
        merge_sort(right)

        l = 0
        r = 0
        for i in range(len(items)):
            # lval = left[l] if l < len(left) else None
            if l < len(left):
                lval = left[l]
            else:
                lval = None

            # rval = right[r] if r < len(right) else None
            if r < len(right):
                rval = right[r]
            else:
                rval = None

            if (lval and rval and lval < rval) or rval is None:
                items[i] = lval
                l += 1
            elif (lval and rval and lval >= rval) or lval is None:
                items[i] = rval
                r += 1

    return items
