def get_slargest_sSmallest(lst):
   

    max_val = min_val = lst[0]
    

    for i in lst:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i


    second_largest = min_val
    second_smallest = max_val


    for i in lst:
        if i != max_val and i > second_largest:
            second_largest = i


    for i in lst:
        if i != min_val and i < second_smallest:
            second_smallest = i


    return second_largest, second_smallest

print(get_slargest_sSmallest([1, 2, 3, 4, 5]))
