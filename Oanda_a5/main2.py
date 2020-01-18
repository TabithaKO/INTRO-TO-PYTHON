import BioDNA3
import os
import glob

#Here's where I get to run the code I created in BioDNA3 and hopefully comeup with an output file
def main():
    #Step 1: Print the Title to welcome users to my program
    #This is the title of my program
    Title = BioDNA3.printTitle()
    print(Title) 
    
    #This checks for the number of characters to use for an Lmer
    Lmer = BioDNA3.readLMERfromKeyboard()    
    
    # input directory (that holds all the files)
    inputDIRECTORY = "inputDirectory"	
			    
    # combine a directory path and a filename together into one path
    # get all filenames in this directory ending with a .fna extension 
    
    fullPath = os.path.join(inputDIRECTORY, "*.fna")	
    fileList = glob.glob(fullPath)
	    
    fileList.sort()
    
    print ("\n\nFILES in directory: ", inputDIRECTORY)
    
    for nextFile in fileList:
	    # open the FILE in this directory
	    INPUT = open(nextFile, 'r')
	    print ("\t", nextFile)
	    #To get the next file that contains DNA that needs checking
	    DNA = BioDNA3.getDNA(nextFile)
	    print(DNA)
	    print("Done.")
	
	    
	    #print out my DNA list for checking
	    DNAlist = BioDNA3.breakIntoMotifs(DNA, Lmer)
	    print(DNAlist)
	    
	    #Print out my dictionary for checking
	    Dic =  BioDNA3.createDictionary(DNAlist)
	
	    print(Dic)
	    
	    FinalOutput = BioDNA3.writeOutputToAFile(nextFile,DNAlist,Dic)
  	    
	    
    
    # end for each file in fileList
    
    print ("\nDone.\n\n")        
    
  
   

# end main()


main()
