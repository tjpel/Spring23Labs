GAP_PENALTY = 4
MISMATCH = -3
MATCH = 2

seq1 = "AAC"
seq2 = "AAC"

"""
0seq1    A C
s      A
e      A
q      C
2
"""
def sequenceAlign(s1, s2):
    output = [[-1*GAP_PENALTY*i for i in range(len(s1)+1)]] #makes the top boundry

    for y in range(1, len(s1)+1):
        print("Y is " + str(y) + ", making the side " + str(-1*GAP_PENALTY*y))
        print("Output looks like this:")
        print(output)
        newLine = [-1*GAP_PENALTY*y] #sets the first number for the boundry+1
        for x in range(1, len(s2)+1):
            tempOutput = output
            tempOutput.append(newLine)
            options = [(tempOutput[y][x-1] - GAP_PENALTY),
                    (tempOutput[y-1][x] - GAP_PENALTY), 
                    (tempOutput[y-1][x-1] + checkMatch(seq2[y-2],seq1[x-2]))]
            #newLine.append(max(options))
            max = options[0]
            for o in options:
                if o > max:
                    max = 0
            newLine.append(max)
    print("Adding a new line to output")
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

print(sequenceAlign("AAC", "AAC"))