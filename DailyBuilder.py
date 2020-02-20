import re
import mailbox
mbox_file = "ProblemsExport.mbox"
mbox = mailbox.mbox(mbox_file)
for key in mbox.iterkeys():
    try:
        message = mbox[key]
    except mbox.errors.MessageParseError:
        continue  # skip the oof ones
    #if subject is a Daily Coding Problem
    if subject.startswith("Daily Coding Problem"):
        number = ubject.split("#")[1].split("[")[0][:-1]
        problem = str(message).split("Good morning!")[1].split("\nUpgrade to premium\n[https")[0] #this is lazy, should be using RE
        difficulty = subject.split("[")[1].split("]")[0]
        #print ("Subject:" + subject)
        #print("Number:" + number)
        #print("Difficulty:" + difficulty)
        #print("Content: " + problem)
        #print("********************************************")

        #problem = re.search('Good Morning!(.*) \n\n--',str(message)).group(0)
        #print("Content: "+problem)
        #example regex guesstimate

        
	#create directory called Problem### ex Problem1,Problem2,Problem3...
        direct = "Problem" + number
	if not os.path.exists(direct):
		print("The directory "+ direct + " does already exists")
	else:
		os.mkdir(direct)    
	#create README
        #insert Good morning!+problem
    
