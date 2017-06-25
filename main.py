"""Julia set generator """
import time
from matplotlib import pyplot as plt
import numpy as np

#area of complex space to investigate
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.3, -0.99

def calc_pure_python(width, max_iter):
    """Create a list of complex coordinates (zs) and complex parameters (cs)
    build Julia set, and display"""
    x_step = (float(x2-x1)/float(width))
    y_step = (float(y1-y2)/float(width))
    x = []
    y = []
    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step
    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step
    zs = []
    cs = []
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))

    print "length of x: ", len(x)
    print "total elements: ", len(zs)
    start_time = time.time()

    output = calculate_z_serial_purepython(max_iter, zs, cs)
    #output is a one dimensional list containing each number of types the iteration
    #was proceeded, for each coordinates
    #it has length 1M, 1000x1000
    fout = open('julia.pgm', 'w')
    fout.write('P2\n# Julia Set image\n' + str(1000) + ' ' + str(1000) + '\n300\n')
    for i in range(1000):
        for j in range(1000):
             fout.write(str(output[(i+1)*j+j]) + ' ')
        fout.write('\n')
    fout.close()
    secs = time.time()-start_time
    print calculate_z_serial_purepython.func_name + "took ", secs, "seconds"
    # This sum is expected for a 1000^2 grid with 300 iterations.
    # It catches minor errors we might introduce when we're
    # working on a fixed set of inputs.
    assert sum(output) == 33219980

def calculate_z_serial_purepython(max_iter, zs, cs):
    """calculate output using Julia's update rule"""
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while abs(z) < 2 and n < max_iter:
            z = z * z + c
            n += 1
        output[i] = n
    return output

if __name__ == "__main__":
    #Calculate the julia set using pure python solution
    # for line_profiler
    if '__builtin__' not in dir() or not hasattr(__builtin__, 'profile'):
    def profile(func):
    def inner(*args, **kwargs):
    return func(*args, **kwargs)
    return inner
    calc_pure_python(width = 1000, max_iter = 300)
