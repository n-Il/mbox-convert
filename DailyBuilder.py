#Matt Harris
#02/20/2020
#Converting mbox to problems for fun/practice.
import re
import mailbox
import os
mbox_file = "ProblemsExport.mbox"
mbox = mailbox.mbox(mbox_file)
os.mkdir("output")
for key in mbox.iterkeys():
    try:
        message = mbox[key]
    except mbox.errors.MessageParseError:
        continue  # skip the oof ones
    #if subject is a Daily Coding Problem
    subject = str(message['Subject'])
    if subject.startswith("Daily Coding Problem"):
        number = subject.split("#")[1].split("[")[0][:-1]
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
        direct = "output/Problem" + number
        os.mkdir(direct)
        #create README
        readMe = open(direct+"/README","w+")
  	#insert Good morning!+problem
        readMe.write(problem)
        readMe.close()
