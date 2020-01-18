"""Module of DNA processing functions"""

# ----------------------------------------
def complementDNA_to_DNA( DNA ):
    """Returns the complement strand of DNA"""
    
    # get complementary sequence
    changeThese = "ACTG"
    toThese     = "TGAC"
    transTable  = str.maketrans(changeThese, toThese)
    complementaryStrand = DNA.translate(transTable)
    return complementaryStrand
# ----------------------------------------

# ----------------------------------------
def complementDNA_to_RNA( DNA ):
    """Returns the complement strand of RNA"""
    # get complementary sequence
    changeThese = "ACTG"
    toThese     = "UGAC"
    transTable  = str.maketrans(changeThese, toThese)
    complementaryStrand = DNA.translate(transTable)
    return complementaryStrand
# ----------------------------------------

# ----------------------------------------    
def transcribe( DNA ):
    """Simulates transcription by building template strand and then complementing to RNA"""
    
    # gene is on the incoming DNA strand
    # but RNA copy is built off the template strand
    template = complementDNA_to_DNA( DNA )
        
   # print (" DNA: 3'", template, "5'")    
    
    # simulate building of RNA strand from template
    mRNA     = complementDNA_to_RNA( template )
    
    return mRNA
# ----------------------------------------    
    
    
def makeAminoAcidTable( ):
    """Returns a Python Dictionary (hash table) that maps RNA nucleotides to Amino Acid symbols;
    both one letter and three letter symbols are returned; the user will need to parse which of
    these symbols they want to use"""
    
    AAtable = { "UUU":"F|Phe","UUC":"F|Phe","UUA":"L|Leu","UUG":"L|Leu","UCU":"S|Ser","UCC":"S|Ser",
                "UCA":"S|Ser","UCG":"S|Ser","UAU":"Y|Tyr","UAC":"Y|Tyr","UAA":"*|***","UAG":"*|***",
                "UGU":"C|Cys","UGC":"C|Cys","UGA":"*|***","UGG":"W|Trp","CUU":"L|Leu","CUC":"L|Leu",
                "CUA":"L|Leu","CUG":"L|Leu","CCU":"P|Pro","CCC":"P|Pro","CCA":"P|Pro","CCG":"P|Pro",
                "CAU":"H|His","CAC":"H|His","CAA":"Q|Gln","CAG":"Q|Gln","CGU":"R|Arg","CGC":"R|Arg",
                "CGA":"R|Arg","CGG":"R|Arg","AUU":"I|Ile","AUC":"I|Ile","AUA":"I|Ile","AUG":"M|Met",
                "ACU":"T|Thr","ACC":"T|Thr","ACA":"T|Thr","ACG":"T|Thr","AAU":"N|Asn","AAC":"N|Asn",
                "AAA":"K|Lys","AAG":"K|Lys","AGU":"S|Ser","AGC":"S|Ser","AGA":"R|Arg","AGG":"R|Arg",
                "GUU":"V|Val","GUC":"V|Val","GUA":"V|Val","GUG":"V|Val","GCU":"A|Ala","GCC":"A|Ala",
                "GCA":"A|Ala","GCG":"A|Ala","GAU":"D|Asp","GAC":"D|Asp","GAA":"E|Glu",
                "GAG":"E|Glu","GGU":"G|Gly","GGC":"G|Gly","GGA":"G|Gly","GGG":"G|Gly"}
    
    return AAtable
# ------------------------
    

def translate( mRNA, AAtable ):  
    
    protein = """This function converts the proteins in the DNA into amino acids and returns an abbreviated form of the amino acid""" 
    
    startBP = 0
    endBP   = len(mRNA)
    
    nextCodonStart = startBP
    while ( nextCodonStart+3 <= endBP):
        nextCodon = mRNA[nextCodonStart:nextCodonStart+3]
        
        # play ribosome: convert(map) an RNA triple to an amino acid symbol
        nextAA = AAtable[ nextCodon ]
        
        # amino acid symbols come as two types of symbols (3 letter|1 letter);
        # e.g.,  "GAG":"E|Glu" ... thus need to parse out which type of symbol we want
        
        # we want the 3-letter 'Glu' version here
        AAsymbol = nextAA[2:]
        
        # add this AA onto the end of the growing amino-acid (protein) chain
        protein = protein + AAsymbol
        
        # move down to next triple
        nextCodonStart = nextCodonStart + 3
        
    # end while more triples to check
    
    return protein
# ----------------------------------------
    
    
     
        
# end translate()