import sys
import urllib
import urllib.request
import urllib.parse
import re
import sched
import time


URL = 'http://nedroid.com/'
ComicDate = 'March 10th, 2015'

request = urllib.request.urlopen(URL)
puretext = request.read()			#puretext is of type 'byte'
decoded = puretext.decode("utf-8") 	#this changes it from 'byte' to 'str' format so that it can be worked with
foundNewComic = True

#s = sched.scheduler(time.time, time.sleep)
#s.enter(10, 1, timer, (s,))
#s.run()




##If there is a new comic, 
##update the variable that is looked at to see if a new comic has been uploaded
def redefineComicDate():
    arrayOfDates = re.findall('(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d\d(?:st|nd|rd|th)\,\s\d{4}', decoded)
    #Regular expression to find a date in the format of Month Day(th), Year
    
   
    ComicDate = arrayOfDates[0]                  #The first date found by the regular expression is set to the new comic date
    print("The latest comic was posted on: " +ComicDate)
    #return newComicDate




def firstCheck():
    if ComicDate in decoded:
        print("There is no new comic")
        comicCheck = False
        return comicCheck #FALSE            #maybe change to foundNewComic???

        
    else:
        print("There is a new Nedroid comic!")
        comicCheck = True                 #move away from "FirstComicDate"  #maybe change to foundNewComic???
        return comicCheck #TRUE
        

        


def continuousCheck(newComicGate):
    #print("")
    checker = newComicGate
    #every so often, check for new comic
   # checker = True
    if (checker == False):
        #foundNewComic = check()
        #print("using check() in continunousChecker() because checker is false")
        check()
        something = False
        return something

    elif(checker == True):
        print("calling redefineComicDate()")
        redefineComicDate()
        something = True
        return something

    else:
        print("An unknown error has occured. SHUTTING DOWN.")
        input("Hit enter to exit.")
        sys.exit()



def check():
    #print("CHECK IS BEING RUN")
    if ComicDate in decoded:
        comicCheck = False
        #print("ComicDate is in decoded, found using check(), do not print a new date")
        return comicCheck
    else:
        print("There is a new Nedroid comic! [in check()]")     #remove [in check()}
        comicCheck = True
        return comicCheck


def con():
    if (foundNewComic == False):
        print("con(): foundNewComic is False")
        check()
        something = False
        return something

    if (foundNewComic == True):
        print("con(): foundNewComic is True")
        redefineComicDate()
        print("Calling redefineComicDate() in con()")
        something = True
        return something

        



def main():
    foundNewComic = firstCheck()  #IF TRUE, A NEW COMIC IS FOUND AND CONTINUOUS CHECK WILL CALL REDEFINE COMIC DATE, IF FALSE, WILL TRY "check()"
    everyHour = 60**2
    #foundNewComic = False
    
    
    runContinuousCheck = True
    while (runContinuousCheck == True):
        #foundNewComic = continuousCheck(foundNewComic)
        foundNewComic = con()
        time.sleep(5)


    #timer()
    #s.enter(10, 1, timer, (s,))
    #s.run()
    #x = 0
    #while (x is not 1):
    #    input('Hit enter to exit program')
    #    print("Shutting down....")
    #    x = 1

main()


#def timer(sc): 
#    print("Doing stuff...")
#    #do your stuff
#    if (foundNewComic == False):
#        foundNewComic = firstCheck()
#    elif (foundNewComic == True):
#        redefineComicDate()

#    sc.enter(4, 1, timer, (sc,))
#s = sched.scheduler(time.time, time.sleep)
