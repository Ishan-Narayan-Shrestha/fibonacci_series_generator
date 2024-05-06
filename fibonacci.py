

def get_fabonacci_series(num):
    fabonacci_series = [0, 1]


    if not isinstance(num, int):
        return None
    
    elif num <= 0:
        return None

    elif num == 1:
        return [0]
    
    for i in range(num - 2):
        next_item = fabonacci_series[-1] + fabonacci_series[-2]
        fabonacci_series.append(next_item)

    return fabonacci_series