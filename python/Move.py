def move(n):
    return move_iter(n,1)

def move_iter(num,product):
    if num==1:
        return product
    return move_iter(num-1,num*product)
