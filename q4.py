def custom_min(a,b,c):
    return reduce(lambda x, y: x if x<y else y, [a,b,c])