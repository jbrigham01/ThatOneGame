from random import shuffle

def is_sorted(data) -> bool:
    """Determine whether the data is sorted."""
    return all(a <= b for a, b in zip(data, data[1:]))

def bogosort(data) -> list:
    """Shuffle data until sorted."""
    while not is_sorted(data):
        shuffle(data)
        print(data)
        
    return data

bogosort([9,8,7])