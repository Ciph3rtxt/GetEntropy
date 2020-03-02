# Title:  GetEntropy
# Version: 1.1
# Description:  Calculate Shannon Entropy of files to detect encryption and/or steganography.
# Dependancies:  Python3 and Standard Library
# License:  MIT
# Author:  Matt Barr
# Contact:  https://www.f0r3ns1c.com
# Credits:  Kenneth G. Hartman <https://kennethghartman.com/calculate-file-entropy/>

import sys
import math
import os

if len(sys.argv) != 2:
    print("Usage: GetEntropy.py <file or directory>")
    sys.exit()
arguement = sys.argv[1]
print()

# Function:  Read File/Directory
def readfile(filename):
    try:
        file = open(filename, "rb")
        byteArray = list(file.read())
        file.close()
        fileSize = len(byteArray)
        print("Filename: ", filename)
        frequency(byteArray,fileSize)
    except:
        e = sys.exc_info()[1]
        print(e)
        print()

# Function:  Calculate Frequency
def frequency(byteArray,fileSize):
    frequencyList = []
    for b in range(256):
        i = 0
        for byte in byteArray:
            if byte == b:
                i += 1
        frequencyList.append(float(i) / fileSize)
    entropy(frequencyList,fileSize)

# Function:  Calculate Entropy
def entropy(frequencyList,fileSize):
    entropy = 0.0
    for frequency in frequencyList:
        if frequency > 0:
            entropy = entropy + frequency * math.log(frequency, 2)
    entropy = -entropy
    print("Shannon Entropy: ", entropy)
    print("File Size (Megabytes): ", (fileSize / (1024 * 1024)))
    print("Smallest Possible Filesize (Megabytes): ", ((entropy * fileSize) / 8) / (1024 * 1024))


# Main
if ".\\" in arguement or "./" in arguement:
    arguement = os.getcwd()
if "*" in arguement:
    print("Cannot use wildcard.")
    print()
    sys.exit()
elif "/?" in arguement or "-h" in arguement or "--help" in arguement:
    print("Usage: GetEntropy.py <file or directory>")
    print()
    sys.exit()
elif os.path.isfile(arguement):
    readfile(arguement)
    print()
    sys.exit()
elif os.path.isdir(arguement): 
    for root, dirs, files in os.walk(arguement):
        for name in files:
            file = os.path.join(root, name)
            readfile(file)
            print()
    print()
    sys.exit()
else: 
    print("Invalid file or directory")
    print()
    sys.exit()




