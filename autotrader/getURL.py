import urllib.request
import urllib.parse
import random
from bs4 import BeautifulSoup
import time
import re
import sys

sys.path.insert(1, "PATH")
saveFile = "FILE.txt"
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
headers = {"User-Agent": userAgent}
values = {"name": "Chrome"}
data = urllib.parse.urlencode(values)
data = data.encode("ascii")

def pageDownload(URL):
    req = urllib.request.Request(URL, data, headers)
    return urllib.request.urlopen(req).read().decode("utf-8")

def savePage(URL, file):
    req = urllib.request.Request(URL, data, headers)
    page = urllib.request.urlopen(req).read().decode("utf-8")
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
    for i in range(1, 147):
        target = "https://www.autotrader.co.za/cars-for-sale/western-cape/p-9?pagenumber={}&price=100001-to-200000".format(i)
        savePage(target, saveFile)
        extractHREF()
        print("No: {} => Complete".format(i))
        time.sleep(random.randint(15, 30))

#for i in range(len(pagArr))
