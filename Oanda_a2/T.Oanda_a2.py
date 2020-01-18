
import os
from math import exp, log

"""-----------------------------------------------------------------------------
SUMMARY: 
    This program enables one to compute and analyze the various characteristics of a 
given gene sequence. 
It's possible to get the proportions, percentage and even probabilities of given 
nucleotides in the sequence.
Programmer: Tabitha Oanda
    
INPUT:
      This retrieves the DNA string from a source and has it ready for 
    execution by the program. The souce contains the sequence in FASTA format.
     
OUTPUT:
    This program will produce the proportion and percentage of the A, C, T, G 
    nucleotides in the entire sequence.
    The program also computes the number of nucleotides that are not identified 
    as A,C,T or G.
    This program also computes the probability of finding certain nucleotide 
    combinations in the given sequence.
------------------------------------------------------------------------------
"""

 #------- Do NOT change this Python function--------------------------------

def getDNA( filename ):
    """ Open a FASTA file of DNA read it, and return the DNA as one string.
    
    Function to open a FASTA formatted file of DNA sequence, remove
    first (header) line and newline characters, and return as one (long) string.
    
    Argument:  one(1) string with the name of a FASTA-formtted file of DNA.
    Returns:   entire sequence of DNA as one string
 
    A sample of how you might "call" this funciton from your program
    to 'get' the DNA for chromosome III of the worm, C.elegans.
 
    sequence = getDNA("worm_III.fna")

    Note: This function (sometimes called a subroutine) is ready for you
    to use in your program. Think of this routine as a "button on your
    calculator" ... this is ready for to use. When you "use" this
    routine, we say "your program is CALLING" for the use of that routine.
    -----------------------------------------------------------------------
    
    """
    # make sure there really *is* a filename with this name
    if (not os.path.isfile(filename)):
        print ("No file found in current directory named: ", filename)
        return ""
    else:
        DNA = ""
        with open(filename) as INPUT:
            next(INPUT)  # skip the header line
            # now read all the other lines in the file
            for nextLine in INPUT: 
                nextLine = nextLine.strip()  # remove the newline
                DNA = DNA + nextLine
            # end for each line
                
            return DNA
    # end else
    
# end getDNA()
# ------------------------------------------------------------------------
    
    
def main():    
    
    #inputGenomeFile = "test1.fna"
    # or
    #inputGenomeFile = "Nanoarchaeum_equitans_Kin4_M.fna"
    # or
    #inputGenomeFile = "EcoliK12_genomic.fna"
    inputGenomeFile = "Acetobacterascendens_genomic.fna"
    #inputGenomeFile = "test2.fna"
    # inputGenomeFile = "put your file name here"
    
    # get the DNA sequence from a file and store in a Python string
    sequence = getDNA( inputGenomeFile )
     
    # don't run this next line if you have a huge genome!
    #print ("\nDNA: ", sequence, "\n")
    
    DNA = sequence.upper()
    DNAlength = len(DNA)
    print("\nTotal length of DNA:\t", DNAlength, "bp")
    numberofA = DNA[:].count("A")
    print ("\nThe number of Adenine nucleotides is ", numberofA)
    numberofC = DNA[:].count("C")
    print ("\nThe number of Cytosine nucleotides is ", numberofC)
    numberofG = DNA[:].count("G")
    print ("\nThe number of Guanine nucleotides is ", numberofG)
    numberofT = DNA[:].count("T")
    print ("\nThe number of Thymine nucleotides is ", numberofT)
    print ("-"*40)
    totalnumber = len(DNA)
    print ("The total number of nucleotides is ", totalnumber)
    anonymous = totalnumber-(numberofA + numberofC + numberofG + numberofT)
    print ("The total number of nucleotides that are not A,C,G,or T is ", anonymous)
    print ("-"*40)
    proportionA = numberofA / totalnumber
    print ("The proportion of A is %0.5f" % proportionA)
    proportionC = numberofC / totalnumber
    print ("The proportion of C is %0.5f " % proportionC)
    proportionG = numberofG / totalnumber
    print ("The proportion of G is %0.5f" % proportionG)
    proportionT = numberofT / totalnumber
    print ("The proportion of T is %0.5f" % proportionT)
    print ("-"*40)
    percentageA = proportionA *100
    print ("The percentage of A is %0.5f" % percentageA,"%")
    percentageC = proportionC *100
    print ("The percentage of C is %0.5f " % percentageC,"%")
    percentageG = proportionG *100
    print ("The percentage of G is %0.5f" % percentageG,"%")
    percentageT = proportionT *100
    print ("The percentage of T is %0.5f" % percentageT,"%")
    print ("-"*40)
    percentageAT = (percentageA + percentageT)
    percentageGC = (percentageG + percentageC)
    print ("The percentage of GC is %0.5f" % percentageGC)
    print ("The percentage of AT is %0.5f" % percentageAT)
    print ("-"*40)
    import math
    pA = math.log(proportionA)
    pC = math.log(proportionC)
    pG = math.log(proportionG)
    pT = math.log(proportionT)
    # P1 is the probability of ACGTACGT calculated by adding the logs of the other probabilities
    #P2 is the second step where I raise e to the power of the log total (in P1) to eliminate the logs
    P1 = (pA + pC + pG + pT)
    P2 = math.exp(P1)
    print ("The probability of 'ACGTACGT' in the sequence is: %0.7ef " % P2)
    #100000 bp is my starting point
    #4*10^6 bases are in 1mm of DNA
    #10mm are in 1cm
    #100cm are in 1m
    bp2mm = 100000 /(4*10**6)
    mm2cm = bp2mm / 10
    cm2m = mm2cm / 100
    print ("-"*40)
    print ("The length in cm is ", mm2cm)
    print ("The length in m is ", cm2m)
    
main()
