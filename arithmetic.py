 def list_create():
    li = list(range(1, 11))
    return li

print(list_create())

def add_num():
    list_create()
    total = 0
    for num in range(len(list_create())):
        total += list_create()[num]
    return total
    
print(add_num())

def prod_num():
    list_create()
    product = 1
    for num in range(len(list_create())):
        product *= list_create()[num]
    return product
    
print(prod_num())

def avg_num():
    list_create()
    total = 0
    for num in range(len(list_create())):
        total += list_create()[num]
        avg = total/len(list_create())
    return avg
    
print(avg_num())

def split_avg():
    list_create()
    total = 0
    for num in range(len(list_create())//2, len(list_create())):
        total += list_create()[num]
        avg = total/(len(list_create())//2)
    return avg

print(split_avg())