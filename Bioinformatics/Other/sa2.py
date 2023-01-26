GAP_PENALTY = 5
MISMATCH = -3
MATCH = 2

def seqAli(s1: str, s2: str) -> list:
    #s1 becomes x
    #s2 becomes y
    output = [[-1*GAP_PENALTY*x for x in range(len(s1)+1)]]
    for y in range(1,len(s2)+1):
        newLine = [-1*GAP_PENALTY*y]
        for x in range(1, len(s1)+1):
            tempOutput = output.copy()
            tempOutput.append(newLine)
            options = [(tempOutput[y][x-1] - GAP_PENALTY),
                    (tempOutput[y-1][x] - GAP_PENALTY), 
                    (tempOutput[y-1][x-1] + checkMatch(s2[y-1],s1[x-1]))]
            newLine.append(max(options))
        output.append(newLine)
    return output

def checkMatch(a: str, b: str) -> int:
    if a == b:
        return MATCH
    return MISMATCH

def printAlign(alignment: list):
    for i in range(len(alignment)):
        for j in range(len(alignment[i])):
            print(alignment[i][j], end=" ")
        print("")

def getAlignment(alignment: list, s1: str, s2: str):
    y = len(s1)
    x = len(s2)
    current = alignment[y][x]
    output = ""
    while(len(s1) != len(s2)):
        current = alignment[y][x]
        if((alignment[y-1][x-1] == current-MATCH) or (alignment[y-1][x-1] == current-MISMATCH)):
            output += s2[y]
            x -= 1
            y -= 1
        elif(alignment[y-1][x] == current+GAP_PENALTY):
            output += "-"
            y -= 1
        else:
            output += "-"
            x -= 1
        print(output[::-1])
    return output[::-1]

s1 = "AATCG" #longer
s2 = "AACG" #shorter

alignment = seqAli(s1, s2)

printAlign(alignment)
#exact = getAlignment(alignment, s2, s1)
#print(exact)
