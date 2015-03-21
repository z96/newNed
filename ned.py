import sys
import urllib
import urllib.request
import urllib.parse
import re

URL = 'http://nedroid.com/'
FirstComicDate = 'March 10th, 2015'

request = urllib.request.urlopen(URL)
puretext = request.read()			#puretext is of type 'byte'
decoded = puretext.decode("utf-8") 	#this changes it from 'byte' to 'str' format so that it can be worked with

FirstComicDate = 'March 10th, 2015'
checkForNewDate = False

TEST = 'string test'


##If there is a new comic, 
##update the variable that is looked at to see if a new comic has been uploaded
def redefineComicDate(check):
    if (check == True):
        arrayOfDates = re.findall('(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d\d(?:st|nd|rd|th)\,\s\d{4}', decoded)
                                                        #Regular expression to find a date in the format of Month Day(th), Year
        newComicDate = arrayOfDates[0]                  #The first date found by the regular expression is set to the new comic date
        print("This comic was posted on: " +newComicDate)
        #return newComicDate


def firstCheck():
	if FirstComicDate in decoded:
		print("There is no new comic")
	else:
		print("There is a new Nedroid comic!")
		checkForNewDate = True
		redefineComicDate(checkForNewDate)			#this is where redefineComicDate happens



def main():

    firstCheck()
    x = 0
    while (x is not 1):
        input('Hit enter to exit program')
        print("Shutting down....")
        x = 1


main()