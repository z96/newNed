import sys
import urllib
import urllib.request
import urllib.parse
import re
import sched
import time


url = 'http://nedroid.com'
global latestComicDate
global comicDate

request = urllib.request.urlopen(url)
puretext = request.read()
decoded = puretext.decode("utf-8")


def newCheck(x,y):
    if x == y:  #if comicDate == latestComicDate
        return False #there is no new comic
    else:
        return True  #there is a new comic



#find dates in webpage
def dateUpdate():
    arrayOfDates = re.findall('(?:January|February|March|April|May|June|July|August|September|October|November|December)(?:\s|\d)\d(?:st|nd|rd|th)\,\s\d{4}', decoded)
    newComicDate = arrayOfDates[0]
    return newComicDate


def main():
    latestComicUpdate = "June 3rd, 2015"
    comicDate = dateUpdate()
    new = newCheck(comicDate, latestComicUpdate)


    if new == True:
        print("A new comic was posted on " + comicDate)
        print("Visit http://nedroid.com to view the new comic!")
    if new == False:
        print("There is no new comic. The last comic was posted on "+comicDate)
    else:
        print("There was an unexpected error!")
        break


    time.sleep(10)




main()






