def bubble_sort(items):
    n = len(items)
    for i in range(n-1,0,-1):
        for j in range(i):
            if items[j] > items[j+1] :
                items[j], items[j+1] = items[j+1], items[j]
    return items

    '''Return array of items, sorted in ascending order'''
def merge_sort(items):
    if len(items) < 2:return items

    result,mid = [],int(len(items)/2)

    y = merge_sort(items[:mid])
    z = merge_sort(items[mid:])

    while (len(y) > 0) and (len(z) > 0):
            if y[0] > z[0]:result.append(z.pop(0))
            else:result.append(y.pop(0))

    result.extend(y+z)
    return result


    '''Return array of items, sorted in ascending order'''
def quick_sort(items):
    if len(items) == 0:
        return items
    start = items[0]
    first = [x for x in items if x == start]
    smaller = quick_sort([x for x in items if x < start])
    larger = quick_sort([x for x in items if x > start])
    return smaller + first + larger
