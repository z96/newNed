import sys
import urllib
import urllib.request
import urllib.parse
import re

URL = 'http://nedroid.com/'
request = urllib.request.urlopen(URL)
TEST = 'string test'


#If there is a new comic, 
#update the variable that is looked at to see if a new comic has been uploaded

def redefineComicDate(check):
    if (check == True):
        arrayOfDates = re.findall('(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d\d(?:st|nd|rd|th)\,\s\d{4}', decoded)
        #Regular expression to find a date in the format of Month Day(th), Year
        newComicDate = arrayOfDates[0] #The first date found by the regular expression is set to the new comic date
        print("The new 'comic date' is: " +newComicDate)
        #return newComicDate
        
        


def firstCheck():
	if FirstComicDate in decoded:
		print("There is no new comic")
	else:
		print("There is a new Nedroid comic!")
		checkForNewDate = True
		redefineComicDate(checkForNewDate)			#this is where redefineComicDate happens



puretext = request.read()			#puretext is of type 'byte'
decoded = puretext.decode("utf-8") 	#this changes it from 'byte' to 'str' format so that it can be worked with
FirstComicDate = 'March 10th, 2015'
checkForNewDate = False

		
		
firstCheck()
#print(newComicDate)
	
	
x = 0
while (x is not 1):
    input('Hit enter to exit program')
    x = 1
    

print("Shutting down......")



#variables outside of this will print in this function
def main():
	DO_NOT_END = 1
	while (DO_NOT_END == 1):
		print("breaking ned")
		break

main()




##response = urlopen(request)
##response = urllib.urlopen(request)
##url_handle = urllib.urlopen(request)
##headers = urllib.url_handle.info()