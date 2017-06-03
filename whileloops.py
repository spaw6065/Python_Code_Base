
#uploadedelements = ['EMPDTLS.sql','README.md','askme.py','cgitest.py','cmdargs.py','copy_files.txt','copyfile.py','exp1.py','file2.txt','files.txt','functions.py','helloworld.py','helloworld.py','keylogger.py','openGC.py','pyodbc_connect.py','rawinput.py','readfile.py','webpage.py']
#allelements=['askme.py','breakwords.py','breakwords.pyc','cgitest.py','cmdargs.py','copyfile.py','copy_files.txt','EMPDTLS.sql','ex25.py','ex25.pyc','exercise1.py','exp1.py','file2.txt','files.txt','forloops.py','functions.py','helloworld.html','helloworld.py','ifelsestmts.py','JARVIS.py','keylogger.py','openGC.py','pyodbc_connect.py','rawinput.py','readfile.py','SendEmail.py','SendEmailp.py','tempfileslist.txt','webpage.py','whileloops.py']

allelements=['ifelsestmts.py']
uploadedelements = ['EMPDTLS.sql']

def sortedlist(inputlist):
    return sorted(inputlist)

def uploadgithub(filefullpathname):
    g = Github("spaw6065", "Psumit88@")
    repo = g.get_user().get_repo('Python_Examples')

    commit_message = 'Add simple regression analysis'

    tree = repo.get_git_tree(sha)
	
    repo.create_git_commit(commit_message, tree, filefullpathname)
    repo.push()

sort_uploadedelements = sortedlist(uploadedelements)
sort_allelements = sortedlist(allelements)

countofallelements = 0;

print "------------------------------------------------------------------------------------"

for iallelements in sort_allelements:
    #print "Content of all elements list %r" % sort_allelements[countofallelements]

    countofuploadedelements = 0;
    ElementPresent = False

    for iuploadedelements in sort_uploadedelements:
        #print "Content of uploaded elements list %r" % sort_uploadedelements[countofuploadedelements]
        
        if sort_allelements[countofallelements] == sort_uploadedelements[countofuploadedelements]:
            ElementPresent = True
            break
        else:
            ElementPresent = False
        countofuploadedelements = countofuploadedelements + 1

    if ElementPresent == False:
        print "Element %r not present in uploadedelement list"% (sort_allelements[countofallelements])
		#uploadgithub(
    countofallelements = countofallelements + 1

print "------------------------------------------------------------------------------------"
print "Total files present in allelements list %r"% countofallelements
print "Total files present uploadedelements list %r"% countofuploadedelements
print "------------------------------------------------------------------------------------"