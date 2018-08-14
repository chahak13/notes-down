import os
import urllib.request
import requests
from bs4 import BeautifulSoup

def intranetSpider(folderURL, baseDir):
    '''
    This function checks the files present in the intranet folder provided in the folderURL variable and downloads the files that are not present in the folder.
    It also sends a notifiation to the user's desktop containing the file name which was downloaded and the folder where it was downloaded.
    '''

    # url = "http://intranet.daiict.ac.in/~daiict_nt01/Lecture/Arnab%20Kumar/Winter/SC465/lecture_notes/2-Dimension/"


    url = folderURL
    sourceCode = requests.get(url)
    if sourceCode.status_code == 200:
        plainText = sourceCode.text
    else:
        raise ValueError("Couldn't reach the webpage.")
    soup = BeautifulSoup(plainText, "lxml")

    print("Inside folder: ", folderURL)

    basePath = baseDir
    invalidLinks = "?/"
    for link in soup.findAll('a'):
        filename = link.get('href')
        if(filename[0] not in invalidLinks):
            if os.path.isfile(basePath + filename):
                # print(filename,'is present')
                continue
            else:
                fileUrl = url + filename
                try:
                    urllib.request.urlretrieve(fileUrl, basePath+filename)
                except IsADirectoryError:
                    # print("Is a directory error")
                    if os.path.isdir(basePath+filename):
                        # print()
                        # print(filename,'is present')
                        # print()
                        pass
                    else:
                        # print("Made directory: ", filename)
                        os.system('mkdir '+basePath+filename)
                    intranetSpider(folderURL+filename, basePath+filename)
                    # print("Past spider command")
                # print(filename,'downloaded.')
                os.system('notify-send "'+filename+'" "'+filename+' was downloaded to your directory"' )

    return

if __name__ == '__main__':
    folderURL = "http://intranet.daiict.ac.in/~daiict_nt01/Lecture/ANISH%20MATHURIA/IT486/"
    baseDir = "/home/chahak/Documents/Blockchain/"
    if os.path.isdir(baseDir):
        continue
    else:
        os.mkdir(baseDir)
    intranetSpider(folderURL, baseDir)
