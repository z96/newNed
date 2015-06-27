import sys
import urllib
import urllib.request
import urllib.parse
import re
import sched
import time


url = 'http://nedroid.com'
latestComicDate = 'May 3rd, 2015'


print("original 'latestComicDate' = "+ latestComicDate)


request = urllib.request.urlopen(url)
puretext = request.read()
decoded = puretext.decode("utf-8")



def test():
    arrayOfDates = re.findall('(?:January|February|March|April|May|June|July|August|September|October|November|December)(?:\s|\d)\d(?:st|nd|rd|th)\,\s\d{4}', decoded)
    
    #Regular expression to find a date in the format of Month Day(th), Year 
    ComicDate = arrayOfDates[0]                  #The first date found by the regular expression is set to the new comic date
    print("The latest comic was posted on: " +ComicDate)

    latestComicDate = ComicDate
    print("latestComicDate = "+latestComicDate)
    return ComicDate, latestComicDate




def main():
    test()
    if 'May 3rd, 2015' in latestComicDate:
        print("Latest comic date did not update")
    time.sleep(10)





main()