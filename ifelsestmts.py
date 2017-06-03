def AcceptUserInput():
    value1 = raw_input("Enter number 1 :")
    value2 = raw_input("Enter number 2 :")
    return (value1,value2)

iNum1,iNum2 = AcceptUserInput()

print "iNum1 is %r"% iNum1

if iNum1 in range(1, 20) and iNum2 in range(1, 20):
    print "iNum is in the range 1 to 20"

    if iNum1 == iNum2:
        print "you have entered %r and %r and both are equal"% (iNum1,iNum2)
    elif iNum1 <= iNum2:
	    print "you have entered %r and %r and %r less than %r"% (iNum1,iNum2,iNum1,iNum2)
    else:
        print "you have entered %r and %r and both are not equal "% (iNum1,iNum2)
