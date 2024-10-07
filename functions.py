def reverse_list(lst: list) -> list:
    return lst[::-1]

def repeat_twice(lst: list) -> list:
    return lst * 2

def move_3_right_2(lst: list) -> list:
    indexes = [i for i in range(len(lst)) if lst[i] == 3]
    new_lst = lst[:]
    for ix in indexes:
        new_ix = (ix + 2) % len(lst)
        old_val = lst[new_ix]
        new_lst[new_ix] = 3
        new_lst[ix] = old_val
    return new_lst

def replace_first_with_7(lst: list) -> list:
    first_val = lst[0]
    new_lst = lst[:]
    for i in range(len(lst)):
        if lst[i] == first_val:
            new_lst[i] = 7
    return new_lst

def replace_first_with_last(lst: list) -> list:
    first_val = lst[0]
    last_val = lst[-1]
    new_lst = lst[:]
    for i in range(len(lst)):
        if lst[i] == first_val:
            new_lst[i] = last_val
    return new_lst

def spiral_rotate(lst: list) -> list:
    if len(lst) <= 1:
        return lst
    
    n = len(lst)
    mid = n // 2
    new_lst = [0] * n
    
    for i in range(n):
        if i < mid:
            new_index = (i * 2 + 1) % n
        else:
            new_index = ((n - 1 - i) * 2) % n
        new_lst[new_index] = lst[i]
    
    return new_lst

def zigzag_shuffle(lst: list) -> list:
    if len(lst) <= 2:
        return lst
    
    result = []
    left, right = 0, len(lst) - 1
    
    while left < right:
        result.append(lst[left])
        result.append(lst[right])
        left += 1
        right -= 1
    
    if left == right:
        result.append(lst[left])
    
    return result

def consecutive_to_zeros(lst: list) -> list:
    if len(lst) <= 1:
        return lst
    
    result = []
    count = 1
    
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            count += 1
        else:
            if count > 1:
                result.extend([0] * count)
            else:
                result.append(lst[i-1])
            count = 1
    
    if count > 1:
        result.extend([0] * count)
    else:
        result.append(lst[-1])
    
    return result

def consecutive_to_last(lst: list) -> list:
    if len(lst) <= 1:
        return lst
    
    last_value = lst[-1]
    result = []
    count = 1
    
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            count += 1
        else:
            if count > 1:
                result.extend([last_value] * count)
            else:
                result.append(lst[i-1])
            count = 1
    
    if count > 1:
        result.extend([last_value] * count)
    else:
        result.append(lst[-1])
    
    return result

def group_replace_with_first(lst: list) -> list:
    if not lst:
        return lst

    result = []
    current_group_start = 0

    for i, num in enumerate(lst):
        if num == 0 or i == len(lst) - 1:
            group = lst[current_group_start:i + 1]
            first_in_group = group[0]
            result.extend([first_in_group] * (len(group) - 1))
            if num == 0:
                result.append(0)
                current_group_start = i + 1
            elif i == len(lst) - 1:
                result.append(first_in_group)

    return result
