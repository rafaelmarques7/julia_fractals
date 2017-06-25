"""Julia set generator without optional PIL-based image drawing"""
import time
import math
# area of complex space to investigate
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
r = 0.7885
a = 0.2*math.pi
c_real = r*math.cos(a)
c_imag = r*math.sin(a)
#c_real, c_imag = -0.4569, -0.457

def calc_pure_python(desired_width, max_iterations):
    """Create a list of complex coordinates (zs) and complex
    parameters (cs), build Julia set, and display"""
    x_step = (float(x2 - x1) / float(desired_width))
    y_step = (float(y2 - y1) / float(desired_width))
    x = []
    y = []
    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord -= y_step
    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step
    # Build a list of coordinates and the initial condition for each cell.
    # Note that our initial condition is a constant and could easily be removed;
    # we use it to simulate a real-world scenario with several inputs to
    # our function.
    zs = []
    cs = []
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))
            
    print "Length of x:", len(x)
    print "Total elements:", len(zs)
    
    start_time = time.time()
    output = calculate_z_serial_purepython(max_iterations, zs, cs)

    fout = open('julia.pgm', 'w')
    fout.write('P2\n# Julia Set image\n' + str(1000) + ' ' + str(1000) + '\n300\n')
    for i in range(1000):
        list_part = output[i*1000:i*1000+1000]
        for item in list_part:
            fout.write(str(item) + ' ')
        fout.write('\n')
    fout.close()
    
    end_time = time.time()
    secs = end_time - start_time
    print calculate_z_serial_purepython.func_name + " took", secs, "seconds"


def calculate_z_serial_purepython(maxiter, zs, cs):
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

if __name__ == "__main__":
    # Calculate the Julia set using a pure Python solution with
    # reasonable defaults for a laptop
    calc_pure_python(desired_width=1000, max_iterations=300)
