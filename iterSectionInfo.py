import requests
from bs4 import BeautifulSoup
class Info(object):
    URL_1="http://saat.soa.ac.in/section/sectionallotmentdetails.php?REGDNO="
    URL_2="&login="
    FINAL_URL=""
    PAGE=""
    NAME="    No Value Found     "
    SECTION="    No Value Found     "
    BRANCH="    No Value Found     "

    def __init__(self,regno):
        self.FINAL_URL=self.URL_1+regno+self.URL_2
        self.PAGE=requests.get(self.FINAL_URL)
        if self.PAGE.status_code!=200:
            print('Page didn\'t responded ',self.PAGE)
        else:
            self.getVals()

    def getHTML(self):
        return self.PAGE.text

    def getVals(self):
        s=self.getHTML()
        soup = BeautifulSoup(s, 'html.parser')
        arr=soup.findAll('td')
        self.NAME=arr[4]
        self.SECTION=arr[7]
        self.BRANCH=arr[6]

    def getName(self):
        s=str(self.NAME)
        s=s[4:len(s)-5]
        return s

    def getSection(self):
        s=str(self.SECTION)
        s=s[4:len(s)-5]
        return s

    def getBranch(self):
        s=str(self.BRANCH)
        s=s[4:len(s)-5]
        return s