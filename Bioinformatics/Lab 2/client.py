#Thomas Pelowitz
#Lab 2 Bioinformatics
#Winona State University

def countDNA1(s: str):
    """
    Parameters: String s, where s is a DNA nucleotide string of A's, T's, C's, G's
    Output: A dictionary with key value pairs, where the keys are A's, T's, C's, and G's
        and the values are the count of how many times that appears in s
    """
    print(s.count("A"), s.count("T"), s.count("C"), s.count("G"))

def countDNA2(s: str) -> tuple:
    return (s.count("A"), s.count("T"), s.count("C"), s.count("G"))

def countDNA3(s: str) -> list:
    return [s.count("A"), s.count("T"), s.count("C"), s.count("G")]

def changeToRNA1(s: str):
    """
    Parameters: String s, where s is a DNA nucleotide chain of A's, T's, C's, G's
    Output: A string that is similar to s, but the T's are changes to U's to mimic RNA
    """
    print(s.replace("T", "U"))

def changeToRNA2(s: str) -> str:
    return s.replace("T", "U")

def main():
    dna = input("Please enter a DNA seqence:\n")
    countDNA1(dna)

    #print(countDNA2(dna))
    count2 = countDNA2(dna)
    for count in count2:
        print(count, end= ' ')
    print("")

    #print(countDNA3(dna))
    count3 = countDNA3(dna)
    print(count3[0], count3[1], count3[2], count3[3])
    print(f'A\'s count: {count3[0]}, T\'s count: {count3[1]}, C\'s count: {count3[2]}, G\'s count: {count3[3]}')
    print(f"A's count: {count3[0]}, T's count: {count3[1]}, C's count: {count3[2]}, G's count: {count3[3]}")

    changeToRNA1(dna)
    print(changeToRNA2(dna))

if __name__ == '__main__':
    main()
