from sys import argv

def print_all(pFile):
   print pFile.read()

def rewind(pFile,seekpos):
   pFile.seek(seekpos)

def print_a_line(curlineno,pFile):
   print "Current Line number : %d" % curlineno
   print pFile.readline(),


#main process starts here
Filename = raw_input("Enter File name ?")
pFileActual=open(Filename)
print_all(pFileActual)

seekposition = int(raw_input("Enter line number?"))
rewind(pFileActual,seekposition)

currentLineNo = 1
print_a_line(currentLineNo,pFileActual)

currentLineNo = currentLineNo + 1
print_a_line(currentLineNo, pFileActual)

def add(val1,val2):
   print "Entered value1 :%d" % val1
   print "Entered value2 :%d" % val2
   return val1,val2,val1 +  val2

firstno,secondno,addval = add(10,20)
print "Sum is :%d and %d is %d" % (firstno,secondno,addval)