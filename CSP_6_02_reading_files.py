#You must make and submit your own test file and txt file with this assignment.

def toString(fileName):
    #This function returns the text from a given file.
    #Any new lines are written as \n
    f = open(fileName)
    out = ""
    for line in f:
        out += line
    return out

#print(toString("ExampleText.txt")=="Here is the text\ni am another line")
print(toString("ExampleText.txt"))

def longestLine(fileName):
    f = open(fileName)
    longest = 0
    answerLine = ""
    for line in f:
        x = len(line)
        if x > longest:
            longest = x
            answerLine = line
    return(answerLine)


def toBinary(fileName):
    #Given a file that is only 0's and 1's return a list of the file broken into bytes.
    #An example return might be ['01101001', '00101010', '1010']
    f = open(fileName)
    bytes = []

    for line in f:
        line = line.strip()
        for b in range(0, int(len(line/8)):
            bytes.append(line[b*8: (b+1)*8])

        if len(line) - (b+1)*8 > 0:
            bytes.append(line[(b+1)*8 : len(line) ])

    return bytes
