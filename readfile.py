from sys import argv
from os.path import exists

script,filename = argv

##read contents from file
print "You have entered input parameters", argv
print "Running Script 	 : ", script
print "Entered file name: ", filename

txt = open(filename)

print "Contents of file "+ filename
print txt.read()

pDataCopyFile = txt.read()

## copy contents of pfile1 to another file
print "\n\n Started copy of files\n\n"
CopyFileName = raw_input("Enter the copy file name?")

print "Copy File Name :" + CopyFileName

print "Checking if file exists......"
print "File exists status:  %r"% exists(CopyFileName)

pCopyFile = open(CopyFileName,'w')
pCopyFile.write(pDataCopyFile)

#print pCopyFile.read()


## write a new file
#print "##############################"
#filename2 = raw_input("Enter file name : ")
#print "We are opening the file", filename2

#pfile1 = open(filename2,'r+')
#print "We are truncating the file" , filename

#pfile1.truncate()

#print "Provide your input in three lines to write in the file"
#line1 = raw_input("Line 1:")
#line2 = raw_input("Line 2:")
#line3 = raw_input("Line 3:")

#pfile1.write(line1)
#pfile1.write("\n")
#pfile1.write(line2)
#pfile1.write("\n")
#pfile1.write(line3)




