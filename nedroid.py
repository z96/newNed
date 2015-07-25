import sys
import urllib
import urllib.request
import urllib.parse
import re
import sched
import time
import webbrowser


url = 'http://nedroid.com'
request = urllib.request.urlopen(url)
puretext = request.read()
decoded = puretext.decode("utf-8")

def newCheck(x,y):
    if x == y:          #if comicDate == latestComicDate
        return False    #there is no new comic
    else:
        return True     #there is a new comic



#find dates formatted by "Month, Day(st,nd,rd,th) Year" in webpage
def dateUpdate():
    arrayOfDates = re.findall('(?:January|February|March|April|May|June|July|August|September|October|November|December)(?:\s|\s\d)\d(?:st|nd|rd|th)\,\s\d{4}', decoded)                                                                                                                     #space then digit or space then two digits 
    newComicDate = arrayOfDates[0]
    return newComicDate




#################
def main():
    latestComicUpdate = "June 3rd, 2015" #This is the last date a comic was posted at the time of creating this script
    comicDate = dateUpdate()
    new = newCheck(comicDate, latestComicUpdate)


    if new == True:
        print("A new comic was posted on " + comicDate)
        #print("Visit http://nedroid.com to view the new comic!")
        print("Opening to nedroid.com!")
        webbrowser.open(url)

    if new == False:
        print("There is no new comic. The newest comic was posted on "+comicDate)

    time.sleep(10)
##################
    
main()


#notes: use urllib (https://docs.python.org/2/library/urllib.html) to possibly retrieve image
#       and display without opening browser.
