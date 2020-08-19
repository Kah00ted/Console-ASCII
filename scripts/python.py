# A python script to print ASCII art from a file

import sys

file = ""
times = 2
stop = False

try: 
    file = sys.argv[1]
    while (stop == False):
        try:
            file = (file+" "+sys.argv[times])
            times = (times + 1)
        except:
            stop = True
except:
    print ("Usage: ascii.py <input file>")
    exit()

print(file)

try:
    asciiFile = open(file,"r")
except:
    print("Error while attempting to open: ", file)

try:
    asciiText = asciiFile.readlines()
except:
    print("Error while attempting to read: ", file)

try:
    for line in asciiText:
        line = (ascii(line))
        line = line[:-3]
        print(line)
except:
    print("Error while attempting to print from: ", file)
