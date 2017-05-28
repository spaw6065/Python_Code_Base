from sys import argv
scriptname,arg2  = argv
prompt = "> "
print "I am %s script.How can I help you" % scriptname
name = raw_input(prompt)
print "You have entered %s" % name