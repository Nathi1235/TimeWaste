"""
TimeWaste-Interpreter
Author: Nathanael Eiter
https://github.com/Nathi1235

The following program is a Python-Interpreter for
the esotheric programming language "TimeWaste"
https://esolangs.org/wiki/TimeWaste
"""

#import libraries
import datetime
import sys

#lookuptable for certain keywords, and their execute hours
lookuptable = {
    "while"     : datetime.time(0),
    "for"       : datetime.time(1),
    "print"     : datetime.time(2),
    "input"     : datetime.time(3),
    "if"        : datetime.time(4),
    "import"    : datetime.time(5)
}


#main compiler function
def compile(sourcefile):
    program = "import time\n"                   #add time library for sleep function to the 'compiled' program
    artificialTime = datetime.datetime.now().time() #get current time
    for i in sourcefile:                #iterate through the lines of the sourcefile
        keyWord_inText = False
        for j in lookuptable:
            if j in i:                  #check if keyword from lookuptable is in current line
                keyWord_inText = True
                executeTime = lookuptable[j]            #get execute hour from lookuptable
                if executeTime.hour == artificialTime.hour:  #if current hour is execute hour add no delay
                    program += i
                else:
                    #calculate delay to reach execute hour
                    waitingTime = (datetime.timedelta(hours=executeTime.hour)-datetime.timedelta(hours=artificialTime.hour,minutes=artificialTime.minute,seconds=artificialTime.second)).total_seconds()
                    if waitingTime < 0:
                        waitingTime += 24*60*60
                    program += "\t"*i.count("\t")+f"time.sleep({waitingTime})\n"        #add indent and time.sleep() for delay
                    program += i                                                        #add the line from the sourcefile
                    artificialTime = executeTime                                        #update time
        if not keyWord_inText:
            program += i                                                                #if no keyword in the line just add it to the 'compiled' program
    return program


if __name__ == '__main__':
    #read the TimeWaste-Sourcefile
    file = []
    with open(sys.argv[1],"r") as fobj:
        file = fobj.readlines()
    exec(compile(file))                 #execute the 'compiled' programm
