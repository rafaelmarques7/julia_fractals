def calculate_z(maxiter, zs, cs):
    """Calculate output list using Julia update rule"""
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        #a way to optimize the while cycle (which takes almost 36% of this function's time
        #we can change the order of the and verificaton, because n < maxiter is faster
        #than the abs value checking!
        #while abs(z) < 2 and n < maxiter:
        while n < maxiter and abs(z) < 2:
            z = z * z + c
            n += 1
        output[i] = n
    return output
