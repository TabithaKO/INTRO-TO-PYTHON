"""BioDNA : a module of DNA processing functions """
import os
import re
import glob
import operator
import collections

def getDNA( filename ):
    #This function allows us to open a file and read through the long list of DNA
    #We then strip the ends of the DNA and make it a strip of DNA before sending it to other functions
    #This is to make sure there really *is* a filename with this name

    if (not os.path.isfile(filename)):
        print ("No file found in current directory named: ", filename)
        return ""
    else:
        File = open(filename,"r")
        #This next line removes the header so that it's not added to the sequence
        header = File.readline()


        DNA = ""
        for nextline in File:
            nextline = nextline.strip()
            DNA = DNA + nextline




        #DNA = File
        return (DNA)


    # end else

# end getDNA()
# ------------------------------------------------------------------------
def readLMERfromKeyboard():
    #This function enables the user to set the number of characters that will be used in a set
    correct = False
    while correct == False :
        Lmer = int(input("What length should we use? "))
        if Lmer >= 4 and Lmer <= 8:
            print ("You said",Lmer)
            correct = True
        elif Lmer == "":
            print("We'll use the standard length.")
            Lmer == 4
            correct = True
        else:
            print("That answer is out of range.")
    return (Lmer)



#end readLMERfromKeyboard

def printTitle():
    """This prints the title and art at the top of the output"""
    print("="*50)
    print("\n")
    print("\t\t The Gene Detector")
    print("\t\t We detect comparisons")
    print("-. .-.   .-. .-.   .-. .-.   ."*2)
    print("||\|||\ /|||\|||\ /|||\|||\ /|"*2)
    print("|/ \|||\|||/ \|||\|||/ \|||\||"*2)
    print("~   `-~ `-`   `-~ `-`   `-~ `-"*2)
    print("\n")
    print("="*50)


#end printTitle

def breakIntoMotifs(DNA, Lmer):
    #This function breaks your DNA into L-letter words and puts them in a list
    #It creates a loop that keeps taking slices
    DNAlist = []
    i = 0
    while (i + Lmer) <= len(DNA):
        newslice = DNA[i : (Lmer+i)]
        DNAlist.append(newslice)
        i += 1
        #end while
    return (DNAlist)


#end breakIntoMotifs

def createDictionary(DNAlist):
    #This function allows us to populate a dictionary and get the count of the frequency of certain Lmers
    #We're populating the dictionary from the list
    DNADictionary = {}
    for nextLmer in DNAlist:
        nextLmer = nextLmer.lower()
        if nextLmer in DNADictionary.keys():
            # increment that Lmer's count
            DNADictionary[nextLmer] = DNADictionary[nextLmer]+1
        else:
            # first time we’ve seen this Lmer
            DNADictionary[nextLmer] = 1
        
        
    return (DNADictionary)

#end createDictionary


def writeOutputToAFile(Filename, DNAlist,DNADictionary):
    Separater = ','
    # write output to a csv file called Tabitha's Output
    OUTPUT = open("Your Output.csv", 'a')  
    
   
    
    
    # print headers for output
    OUTPUT.write("%s" % ("\n{}\n").format(Filename))
    OUTPUT.write("%s" % ("{}\n").format("Number of motifs: " + str(len(DNAlist))))
    OUTPUT.write("%s%c%s%c%s%c%s\n" % ("Rank", Separater,"Motif", Separater, "Frequency", Separater, "Proportion" ) )

    # print dictionary contents
    i = 1

    # sort your Dictionary by VALUES
    
    sortedDic = sorted(DNADictionary.items(), key=operator.itemgetter(1), reverse = True)
    sortedDic = collections.OrderedDict(sortedDic)    
    n = 0
    for nextLmer in sortedDic.keys():
        n += 1
    
         #Calculating the proportions that will go on the last column
        if n > 10:
            break
         
        proportion = (DNADictionary[nextLmer]/len(DNAlist))
        proportion = ('{0:.4f}'.format(proportion))
        OUTPUT.write("%s%c%s%c%s%c%s\n" % (str(i), Separater, (nextLmer), Separater, sortedDic[nextLmer], Separater, str(proportion) ))
        i =  i+1
        
    
   
   

    OUTPUT.close()

    print("\n\nDone.\n")
    
#end writeOutputToAFile
