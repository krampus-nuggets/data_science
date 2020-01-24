import sys
import csv

sys.path.insert(1, "PATH")
inputFile = "INPUT.csv"
outputFile = "OUTPUT.csv"

def removeBlank():
    with open(inputFile) as inFi:
        with open(outputFile, "w", newline="") as outFi:
            writer = csv.writer(outFi)
            for row in csv.reader(inFi):
                if any(field.strip() for field in row):
                    writer.writerow(row)

if __name__ == "__main__":
    removeBlank()