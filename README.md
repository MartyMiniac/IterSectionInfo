# IterSectionInfo
This python library gets the basic public information about 2019 batch students
## How to use
first download this library into your working directory
*git clone https://github.com/MartyMiniac/IterSectionInfo.git*

### Import the library
*from iterSectionInfo import Info*

### Create an Object
*ob=Info('19410#####')*

### Functions
#### ob.getName() will return the name of the student
#### ob.getSection() will return the section of the student
#### ob.getBranch() will return the branch of the student
#### ob.getHTML() will return the HTML code of the website from which the information is scraped
