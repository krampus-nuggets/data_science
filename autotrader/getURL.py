from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import re
import sys

sys.path.insert(1, "<directory-to-run-script-in-context>")
saveFile = "<file-save-location>"

def pageDownload(URL):
    return urlopen(URL).read().decode("utf-8")

def savePage(URL, file):
    page = urlopen(URL).read().decode("utf-8")
    proc = open(file, "w")
    proc.write(page)
    proc.close()
    return page

def extractHREF():
    with open(saveFile) as file:
        text = file.read()
        soup = BeautifulSoup(text, "html.parser")
        proc = open("URLs.txt" , "a")
        for tag in soup.select("div.e-available>a", href=True):
            hrefTag = tag["href"]
            proc.write("https://www.autotrader.co.za{}\n".format(hrefTag))
        proc.close()

if __name__ == "__main__":
    for i in range(155,165):
        target = "https://www.autotrader.co.za/cars-for-sale/western-cape/p-9?pagenumber={}&price=50001-to-200000".format(i)
        savePage(target, saveFile)
        extractHREF()
        print("No: {} => Complete".format(i))
        time.sleep(10)

#for i in range(len(pagArr))
