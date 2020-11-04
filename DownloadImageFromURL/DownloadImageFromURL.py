##Image File Download, Ideal For Smaller File
##Content Of Image Will Be Read Into Memory At One Go
##Ensure that the module is installed in
## pip3 install fake_useragent
from fake_useragent import UserAgent
import os

##Using Fake_Useragent To Add A HTTP header To The Request
##To Overcome Possible Error Of HTTP Error 403: Forbidden
user_agent = UserAgent()
header = {'User-Agent':str(ua.chrome)}

##Retrieving of filename from URL Path
##Replace Your Directory XXX
url = "XXX"
filename = os.path.basename(urlparse(url).path)

##Replace Your Directory XXX
##Need To Handle Escape Backslash
##"C:\\Folder\\Folder\\"
with open("XXX" + filename, 'wb') as f:
    with urllib.request.urlopen(urllib.request.Request(url, headers=header)) as r:
        f.write(r.read())

#####################################################################################        
        
##A Easy-To-Use 3rd Party Library, Requests
##Ensure that the module is installed in
##Your Python Directory Before You Import
## pip3 install request
## pip3 install fake_useragent
from fake_useragent import UserAgent
import os
import requests

##Using Fake_Useragent To Add A HTTP header To The Request
##To Overcome Possible Error Of HTTP Error 403: Forbidden
user_agent = UserAgent()
header = {'User-Agent':str(ua.chrome)}

##Retrieving of filename from URL Path
##Replace Your Directory XXX
url = "XXX"
filename = os.path.basename(urlparse(url).path)

##Image File Download, Ideal For Smaller File
r = requests.get(url)
##Replace Your Directory XXX
##Need To Handle Escape Backslash
##"C:\\Folder\\Folder\\"
with open("XXX" + filename, "wb") as f:
    f.write(r.content)

##Image File Download, Ideal For Larger File With Streaming
with requests.get(url, stream=True) as r:
    ##Replace Your Directory XXX
    ##Need To Handle Escape Backslash
    ##"C:\\Folder\\Folder\\"
    with open("XXX" + filename, 'wb') as f:
        print("start downloading")
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
            print("downloading")
    print("downloaded")
