def list_create():
    try:
        li = list(range(1, 11))
    except Exception:
        print("The Range must be casted to a list,\
            tuple, set, or dictionary.")
    return li

print(list_create())

def add_num():
    try:
        total = 0
        for num in range(len(list_create())):
            total += list_create()[num]
    except Exception:
        print(f"Wrong. The total is {total}.")
    return total
    
print(add_num())

def prod_num():
    try:
        product = 1
        for num in range(len(list_create())):
            product *= list_create()[num]
    except Exception:
        print("Product can not be set to zero.")
    return product
    
print(prod_num())

def avg_num():
    try:
        total = 0
        for num in range(len(list_create())):
            total += list_create()[num]
            avg = total/len(list_create())
    except Exception:
        print("Zero division error.\
            Numerator can not be divided by 0.")
    return avg
    
print(avg_num())

def split_avg():
    try:
        total = 0
        for num in range(len(list_create())//2, len(list_create())):
            total += list_create()[num]
            avg = total/(len(list_create())//2)
    except Exception:
        print("Zero division error.\
            Numerator can not be divided by 0.")
    return avg

print(split_avg())