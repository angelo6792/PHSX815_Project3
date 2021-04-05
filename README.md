# PHSX815_Project3
Random2.py contains dice roll def

DiceRoll.py conduct a number of experiments using a single dice number of exp(-Nexp #), number of rolls per exp(-Nroll #), changing probabilities(-prob1,2,3,4,5,or6 #) and output files(> filename) can all be changed from the command line. Default dice roll uses Rayleigh distibution for the probabilities of 4-6. 1-3 have a 1/6 probability. probabilities are redistributed to equal 1. Change probabilities from the rayeigh distribution using -seed #

DiceRollAnalysis.py analysis the dice roll data analyze different output files from the command line (python3 DiceRollAnalysis.py -input0 inputfile1name -input1 inputfile2name -seed #(same as DiceRoll))

Can change all probabilites to 1/6 in the command line to compare with fair dice.
