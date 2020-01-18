

import BioDNA

def main():
    
    print ("\n       ---+++ My Really C00l Gene Detector v0.1 +++---\n")
    
    AAtable = BioDNA.makeAminoAcidTable()
    
    #for (tripleRNA, AAcode) in AAtable.items():
        #print (tripleRNA, AAcode)

        
    DNA = "ATGTGTACGCAAATGATATCGTATTAG"

    print("-"*40)
    print ("DNA: 5' " + DNA + " 3'")
    #-----------TRANSLATE----------------
    #Translating is getting the complementary DNA strand
    TDNA = BioDNA.complementDNA_to_DNA(DNA)
    print("DNA: 3'", TDNA ,"5'")
   
    # --------- TRANSCRIBE --------------------------
    #Trancsribing is switching from DNA to RNA
    RNA = BioDNA.transcribe(DNA)
    print (" \t" +"|"*len(DNA))
    print ("mRNA:5'", RNA, "3'")
    
    print ("\n==============================================================")
    print ("Reading Frame #1")
    # --------- TRANSLATE Reading Frame #1 --------------------------
    #CODE for reading frame 1
    #First we find the length of the RNA
    length = len(RNA)
    print ("The RNA length is",length)
    print ("RNA:    ",RNA)
    bars = int(length/3)
    proteins = BioDNA.translate(RNA, AAtable)
    print (" "*10 + "|  "*bars)
    print ("protein:", proteins, "\n")
    front = proteins[0:3]
    end = proteins[-3:]
    middle = proteins[ 3: -3]
    
    if front == ("Met"):
        print ("There is a Met at the start site.")
    else:
        print("There is no Met at the start site.")
        
    if end == ("***"): 
        print("There is a stop at the end.")
    else:
        print("There is no stop at the end.")
        
    if middle.find ("***") != -1:
        print ("There is an interrupting stop.")
        
    else:
        print("There are no interrupting stops.")
    
    if middle.find("Met") != -1:
        print ("There is a Met in the middle")
    else:
        print("There is no Met in the middle")
    
        
    print ("==============================================================\n")
    
    
    print ("\n==============================================================")
    print ("Reading Frame #2")
    # --------- TRANSLATE Reading Frame #2 --------------------------
 
    #CODE for reading frame 2
    DNA2 = DNA[1:]
    RNA2 = BioDNA.transcribe(DNA2) 
    length2 =len(RNA2)
    bars = int(length2/3)
    print ("The RNA length is",length2)
    print ("RNA:    ",RNA2)
    proteins = BioDNA.translate(RNA2, AAtable)
    print (" "*10 + "|  "*bars)
    print ("protein:", proteins, "\n")
    front = proteins[0:3]
    end = proteins[-3:0]
    middle = proteins[ 3: -3]
    
    if front == ("Met"):
        print ("There is a Met at the start site.")
    else:
        print("There is no Met at the start site.")
        
    if end == ("***"): 
        print("There is a stop at the end.")
    else:
        print("There is no stop at the end.")
        
    if middle.find ("***") != -1:
        print ("There is an interrupting stop.")
        
    else:
        print("There are no interrupting stops.")
    
    if middle.find("Met") != -1:
        print ("There is a Met in the middle")
    else:
        print("There is no Met in the middle")
    
    
    
    print ("==============================================================\n")
    
    
    print ("\n==============================================================")
    print ("Reading Frame #3")
    # --------- TRANSLATE Reading Frame #3 --------------------------
    
    #CODE for readif frame 3
    DNA3 = DNA2[2:]
    RNA3 = BioDNA.transcribe(DNA3)
    length3 = len(RNA3)
    bars = int(length3/3)
    print ("The RNA length is",length3)
    print("RNA:    ",RNA3)
    proteins = BioDNA.translate(RNA3, AAtable)
    print (" "*10 + "|  "*bars)
    print("protein:",proteins,"\n")
    front = proteins[0:3]
    end = proteins[-3:0]
    middle = proteins[ 3: -3]    
    
    
    if front == ("Met"):
        print ("There is a Met at the start site.")
    else:
        print("There is no Met at the start site.")
        
    if end == ("***"): 
        print("There is a stop at the end.")
    else:
        print("There is no stop at the end.")
        
    if middle.find ("***") != -1:
        print ("There is an interrupting stop.")
        
    else:
        print("There are no interrupting stops.")
    
    if middle.find("Met") != -1:
        print ("There is a Met in the middle")
    else:
        print("There is no Met in the middle")
    
    
    print ("==============================================================\n")
    
    

        
# --- end main() ---------


#---------------------------------------------------------
# Python starts here ("call" the main() function at start
if __name__ == '__main__':
    main()
#---------------------------------------------------------  

#I nned to have a doc string for the last function in the BIOdna document