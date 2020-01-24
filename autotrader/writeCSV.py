import csv
import sys

sys.path.insert(1, "PATH")
rawFile = "INPUT.txt"
convertedFile = "OUTPUT.csv"

def convertedURLs():
    with open(rawFile, "r") as inputFile:
        stripLines = (line.strip() for line in inputFile)
        lines = (line.split() for line in stripLines if line)
        with open(convertedFile, "w") as outputFile:
            fieldnames = ["HEADERS"]
            writer = csv.writer(outputFile)
            writer.writerow(fieldnames[0:3])
            writer.writerows(lines)

if __name__ == "__main__":
    convertedURLs()
