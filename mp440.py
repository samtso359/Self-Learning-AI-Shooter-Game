from __future__ import division
import inspect
import sys
import numpy
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
'''
Raise a "not defined" exception as a reminder 
'''
def _raise_not_defined():
    print "Method not implemented: %s" % inspect.stack()[1][3]
    sys.exit(1)

'''
Kalman 2D
'''
data = []
iterations = 0
prediction = []
def kalman2d(data):
    estimated = []
    # Your code starts here 
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here
    xk = [0,0]
    Q = [[10 ** (-4), 2 * 10 ** (-5)], [2 * 10 ** (-5), 10 ** (-4)]]
    R = [[10 ** (-2), 5 * 10 ** (-3)], [5 * 10 ** (-3), 2 * 10 ** (-2)]]
    lam = 100000000
    i = [[1, 0],[0,1]]
    pk = [[lam, 0], [0, lam]]

    for ii in range(len(data)):
        u = [data[ii][0], data[ii][1]]
        z = [data[ii][2],data[ii][3]]
        timeP = numpy.add(pk, Q)                #updating time pk
        timeX = numpy.add(xk, u)                #updating time X

        kgain = numpy.matmul(timeP, numpy.linalg.inv(numpy.add(timeP, R)))
        pk = numpy.matmul(numpy.subtract(i,kgain),timeP)
        xk = numpy.add(timeX, numpy.matmul(kgain,(numpy.subtract(z, timeX))))
        estimated.append(xk)



    return estimated

def kalman2dpartB(data):            #with different noise value
    estimated = []
    # Your code starts here
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here
    xk = [0,0]
    Q = [[2, 0.5], [0.5, 2]]
    R = [[200, 50], [50, 300]]
    lam = 100000000
    i = [[1, 0],[0,1]]
    pk = [[lam, 0], [0, lam]]

    for ii in range(len(data)):
        u = [data[ii][0], data[ii][1]]
        z = [data[ii][2],data[ii][3]]
        timeP = numpy.add(pk, Q)                #updating time pk
        timeX = numpy.add(xk, u)                #updating time X

        kgain = numpy.matmul(timeP, numpy.linalg.inv(numpy.add(timeP, R)))
        pk = numpy.matmul(numpy.subtract(i,kgain),timeP)
        xk = numpy.add(timeX, numpy.matmul(kgain,(numpy.subtract(z, timeX))))
        estimated.append(xk)



    return estimated

'''
Plotting
'''
def plot(data, output):
    # Your code starts here 
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here
    z1 =[]
    z2 =[]
    x1 =[]
    x2 =[]
    for i in data:
        z1.append(i[2])
        z2.append(i[3])


    for i in output:
        x1.append(i[0])
        x2.append(i[1])

    plt.plot(z1, z2, 'bo-')
    plt.plot(x1, x2, 'ro-')
    #plt.show()
    return

'''
Kalman 2D 
'''
def kalman2d_shoot(ux, uy, ox, oy, reset=False):
    decision = (0, 0, False)
    global iterations
    if reset:
        iterations = 0
        global data
        data = []
    data.append([ux, uy, ox, oy])


    if iterations == 199:
        prediction = kalman2dpartB(data)
        decision = (prediction[iterations][0],prediction[iterations][1], True)
    iterations = iterations + 1
    return decision

'''
Kalman 2D 
'''
def kalman2d_adv_shoot(ux, uy, ox, oy, reset=False):
    decision = (0, 0, False)
    global iterations
    if reset:
        iterations = 0
        global data
        data = []
    data.append([ux, uy, ox, oy])

    if iterations == 55:
        prediction = kalman2dpartB(data)
        decision = (prediction[iterations][0], prediction[iterations][1], True)
    iterations = iterations + 1
    return decision



