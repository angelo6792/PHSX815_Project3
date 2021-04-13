#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from fractions import Fraction
from scipy.stats import norm

# import our Random class from python/Random.py file
sys.path.append(".")
from Random2 import Random
seed = 5555
# main function for our DiceRollAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    

    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
#        print ("   -input0 [filename]  name of file for H0 data")
#        print ("   -input1 [filename]  name of file for H1 data")
        print
        sys.exit(1)




    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]

    data = np.loadtxt('diceroll1000000')
    Nexp = np.shape(data)[0]
    Nrolls = np.shape(data)[1]

    exp6 = np.array([])
    for i in range(Nexp):
        six = 0
        for j in range(Nrolls):
            if data[i][j] == 6:
                six += 1/Nrolls
        exp6 = np.append(exp6,  six)

    mu, sigma = norm.fit(exp6)
    
    fig, ax = plt.subplots(figsize = (6,6))

    ax.hist(exp6, bins = 8, density = True, histtype = 'step', zorder=1,  linewidth = 1.5)



    x = np.linspace( 0,1, 1000)
    ax.plot(x, norm.pdf(x,mu,sigma), linewidth =2, c ='r')

    ax.vlines(x = mu, ymin = 0, ymax = 10, color = 'k')

    ax.set_xlim([-0.1 , 0.7])
    ax.set_ylim([0, 10])
    ax.set_xlabel('P6', fontsize = 18)
    ax.set_ylabel('Probability', fontsize = 18)
    ax.set_title('100000 experiment', fontsize = 18)
#    plt.show()

    #loads text and put text into an array for the LLR graph
    random = Random(seed)
    RollsH0 = np.loadtxt('diceroll1000000')
    print(len(RollsH0))
    Alpha = 0.35
    a0 = []
    RollH0 = RollsH0.flatten()
    RollH0.sort()
    a0.sort()


    prob1 = Alpha*random.Rayleigh()
    prob2 = Alpha*random.Rayleigh()
    prob3 = Alpha*random.Rayleigh()
    prob4 = Alpha*random.Rayleigh()
    prob5 = Alpha*random.Rayleigh()
    prob6 = Alpha*random.Rayleigh()
    total = prob1+prob2+prob3+prob4+prob5+prob6
    prob1 = prob1 / total
    prob2 = prob2 / total
    prob3 = prob3 / total
    prob4 = prob4 / total
    prob5 = prob5 / total
    prob6 = prob6 / total
    print(prob1)
    print(prob2)
    print(prob3)
    print(prob4)
    print(prob5)
    print(prob6)
    print(mu)
    density0, bins0 =np.histogram(RollH0,bins=np.arange(8)-0.5, density = True)
    unity_density0 = density0 / density0.sum()
    fig, ax = plt.subplots(figsize = (6,6))
    widths = bins0[:-1] - bins0[1:]
    ax.bar(bins0[1:], unity_density0, width=widths, color='blue', alpha = 1.0, align ='edge')

    plt.hist(a0, histtype='bar')
    plt.xlabel('number')
    plt.ylabel('probability')
    plt.title('dice rolls')
    plt.show()


