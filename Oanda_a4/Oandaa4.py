import os
import datetime
import random

# this program opens the given file and sorts the data given into specific lists
#This program then matches data in different lists to each other to find a correlation
def main():
	# ------ CONSTANTS ----------
	READDATA   =  1
	PRINTDATA  =  2
	SIM_X      =  3
	EXIT       =  4
	ERROR      = -1	
	
             
	# ------- Parallel Arrays -------
	firstNames = []
	lastNames  = []
	genders    = []
	ages       = []
	DNAs       = []
		
	#kEEP fILLING tHE lIST tHIS wAY
	
	gotDATA = False  # flag to tell if we've already loaded a datafile
	
	choice = -1  
	while (choice != EXIT):
		print ("\n\n----------------------------------------------")
		print ("  1  -  Read DATA file")
		print ("  2  -  Print DATA file");
		print ("  3  -  Simulation");
		print ("  4  -  EXIT");
		print ("---------------------------")
		choice = input("ENTER: ")
		
		# trap bad user input
		if ( (str(READDATA) <= choice) and (choice <= str(EXIT)) ):
			# force to an integer, for example "1" to 1
			choice = eval(choice)			
		else:
			badInput = choice
			# force to an integer to test below
			choice = ERROR;		
			
		# ============ 1: READ DATA FILE =============================
		#This function reads the data in the file given
		if (choice == READDATA):
			getDATA(firstNames, lastNames, genders, ages, DNAs)
			if (len(firstNames) > 0):
				gotDATA = True
			else:
				print("WARNING: No data read.")
				gotDATA = False
			      # end else			
		
		# ============ 2: PRINT DATA FILE  =============================
		
		elif (choice == PRINTDATA):
			printDATA(firstNames, lastNames, genders, ages, DNAs)

		# ============ 3: SIMULATION =============================
		
		elif (choice == SIM_X):
			theDNA = ""
			sim_DNA(firstNames, lastNames, genders, ages, theDNA, DNAs)
		
		# ============ 4: EXIT =====================================	
		elif (choice == EXIT):
			print ("Goodbye ...")	
		
		# ============ ? HUH ? =====================================
		else:  
			print ("ERROR: ", badInput, "is an invalid input. Try again.")	
	
	# end WHILE input is not EXIT
	
	print ("\n\nDone.\n")
# end main	


#-----------\
# getDATA()  \
#-----------------------------------------------------------
def getDATA( firstNames, lastNames, genders, ages, DNAs ):
	
	dB = input("Enter filename: ")
	if not os.path.exists(dB):
		print("\nSORRY, the file", dB, "does not exist.")
		print("Try another filename ...")
		
	else:	
		print("Read 6 files.")
	File = open("dB1.txt","r")
	
	for nextline in File:
		nextline = nextline.strip()
		pieces = nextline.split(":")
		#print (pieces)
		firstNames.append(pieces[0])
		lastNames.append(pieces[1])
		genders.append(pieces[2])
		ages.append(pieces[3])
		DNAs.append(pieces[4])
		
		
	return(firstNames, lastNames, genders, ages, DNAs)	
		
	File.close()
		
		
	# else filename OK
	
# end getDATA()

#-------------\
# printDATA()  \
#This function prints the data 
#-----------------------------------------------------------
def printDATA( firstNames, lastNames, genders, ages, DNAs ):
	print("+"*20, "Data Summary", "+"*20)
	print("%-11s | %-9s | %-7s | %-5s | %-4s " %("First Name  ", "Last Name", "genders", "ages", "DNAs"))
	print("-"*60)
	for i in range(0,(len(firstNames))):
		print("\n %-11s | %-9s | %-7s | %-5s | %-4s" %(firstNames[i], lastNames[i], genders[i], ages[i], DNAs[i][-10: ]))
	print("+"*60)


# end printDATA()
	

#----------\
# sim_DNA() \
#-----------------------------------------------------------
#This function simulates the new DNA found with the one already existent in the DNAs file
def sim_DNA(firstNames, lastNames, genders, ages, theDNA, DNAs):
	
	File = open("simDoorKnob.txt","r")

	for nextline in File:
		nextline = nextline.strip()
		nextline = nextline.split(",")
		time = nextline[0]
		theDNA = nextline[1]
		result = linearSearch(firstNames, lastNames, genders, ages, theDNA, DNAs)
		location = (DNAs[result]).find(theDNA)
		before = DNAs[result][ :location]
		lower = theDNA.lower()
		after = DNAs[result][location + len(lower): ]
		if result != -1 and (len(theDNA)>= 10):
			print("\n Match Found at",time)
			print ( firstNames[result],"|", lastNames[result],"|", genders[result], "|", ages[result])
			print (before+ lower+ after)
			print("-"*50)
			
			#formatting the output
			
		elif result == -1:
			print ("No match found!")
	File.close()
		
			
	
	
# end sim_DNA()

#-------------\
# linearSearch \
#This function looks for a match in theDNA in the DNAs
#-----------------------------------------------------------
def linearSearch(firstNames, lastNames, genders, ages, theDNA, DNAs):
	i = 0
	found = False
	while i < len(DNAs) and found == False:
		Section = DNAs[i]
		x = Section.find(theDNA)
		if x != -1:
			found = True
			
		
		else:
			i = i + 1
			
	if x == -1:
		return-1
	else:
		return i
	
		
	
# end linearSearch()


	
#-----------\
# START HERE \
#-----------------------------------------------------------	
if (__name__ == '__main__'):
	
	# CONSTANTS
	NOTFOUND = -1
	MIN_DNA_LENGTH = 10
	
	main()

#-----------------------------------------------------
#make a string of DNA and send it through linear search to find out whether it matches  person