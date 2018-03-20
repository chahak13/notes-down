# notes-down
  The *getNotes.py* file uses the _BeautifulSoup_ module and checks the folder provided by the user as the *folderURL* argument in the main function. The *intranetSpider()* function then checks the folder on the intranet and downloads all the files that were not present in the folder on the users' computer. It also shows a notification to the users' computer (supports Ubuntu only at the moment) about the files that have been downloaded and the location it is downloaded to.

  The user can also put this script in the boot options so that whenever the user is connected to the intranet, it will automatically download the files.
