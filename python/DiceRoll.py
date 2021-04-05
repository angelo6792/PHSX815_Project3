#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
from fractions import Fraction 
# import our Random class from python/Random.py file
sys.path.append(".")
from Random2 import Random

# main function for our dice roll Python code
if __name__ == "__main__":
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print
        sys.exit(1)


    # default seed
    seed = 5555
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]

    random = Random(seed)

    # default dice roll  probability with Rayleigh distribution
    prob1 = Fraction(1,6)
    prob2 = Fraction(1,6)
    prob3 = Fraction(1,6)
    prob4 = random.Rayleigh()
    prob5 = random.Rayleigh()
    prob6 = random.Rayleigh()
    total = prob1+prob2+prob3+prob4+prob5+prob6
    prob1 = prob1 / total
    prob2 = prob2 / total
    prob3 = prob3 / total
    prob4 = prob4 / total
    prob5 = prob5 / total
    prob6 = prob6 / total





    # default number of rolls (per experiment)
    Nroll = 1

    # default number of experiments
    Nexp = 1

    # output file defaults
    doOutputFile = False

    # read the user-provided seed from the command line and change dice probabilities (if there)
    if '-prob1' in sys.argv:
        p = sys.argv.index('-prob1')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            prob1 = ptemp
    if '-prob2' in sys.argv:
        p = sys.argv.index('-prob2')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            prob2 = ptemp
    if '-prob3' in sys.argv:
        p = sys.argv.index('-prob3')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            prob3 = ptemp
    if '-prob4' in sys.argv:
        p = sys.argv.index('-prob4')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            prob4 = ptemp
    if '-prob5' in sys.argv:
        p = sys.argv.index('-prob5')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            prob5 = ptemp
    if '-prob6' in sys.argv:
        p = sys.argv.index('-prob6')
        ptemp = float(sys.argv[p+1])
        if ptemp >= 0 and ptemp <= 1:
            prob6 = ptemp
    if '-Nroll' in sys.argv:
        p = sys.argv.index('-Nroll')
        Nt = int(sys.argv[p+1])
        if Nt > 0:
            Nroll = Nt
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Ne = int(sys.argv[p+1])
        if Ne > 0:
            Nexp = Ne
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True


    print(prob1)
    print(prob2)
    print(prob3)
    print(prob4)
    print(prob5)
    print(prob6)

    # class instance of our Random class using seed
    random = Random(seed)

    if doOutputFile:
        outfile = open(OutputFileName, 'w')
        for e in range(0,Nexp):
            for t in range(0,Nroll):
                outfile.write(str(random.Diceroll(prob1,prob2,prob3,prob4,prob5,prob6))+" ")
            outfile.write(" \n")
        outfile.close()
    else:
        for e in range(0,Nexp):
            for t in range(0,Nroll):
                print(random.Diceroll(prob1,prob2,prob3,prob4,prob5,prob6), end=' ')
            print(" ")

