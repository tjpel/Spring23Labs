GAP_PENALTY = 4
MISMATCH = -3
MATCH = 2

seq1 = "AC"
seq2 = "AAC"

"""
0seq1
s
e
q
2
"""
def sequenceAlign(s1, s2):
    output = [[-1*GAP_PENALTY*i for i in range(len(s1)+1)]]

    for x in range(1, len(s1)):
        newLine = [-1*GAP_PENALTY*x]
        for y in range(1, len(s2)):
            tempOutput = output
            tempOutput.append(newLine)
            options = [tempOutput[y][x-1] + checkMatch(seq2[y-1],seq1[x-1]),
                    tempOutput[y-1][x] + checkMatch(seq2[y-1],seq1[x-1]), 
                    tempOutput[y-1][x-1]-GAP_PENALTY]
            newLine.append(max(options))
        output.append(newLine)

    return output

def checkMatch(a,b):
    if a == b:
        return MATCH
    return MISMATCH

def printAlign(alignment):
    for i in range(len(alignment)):
        for j in range(len(alignment[i])):
            print(alignment[i][j], end=" ")
        print("")

printAlign(sequenceAlign("AA", "AACG"))