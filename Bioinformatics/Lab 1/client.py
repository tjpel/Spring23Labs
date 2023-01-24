def countDNA(s: str) -> dict:
    """
    Parameters: String s, where s is a DNA nucleotide string of A's, T's, C's, G's
    Output: A dictionary with key value pairs, where the keys are A's, T's, C's, and G's
        and the values are the count of how many times that appears in s
    """
    return {"A": s.count("A"), "T": s.count("T"), "C": s.count("C"), "G": s.count("G")}

def changeToRNA(s: str) -> str:
    """
    Parameters: String s, where s is a DNA nucleotide chain of A's, T's, C's, G's
    Output: A string that is similar to s, but the T's are changes to U's to mimic RNA
    """
    return s.replace("T", "U")

dna = "GTATCGATCCCAGTTTGACAGGG"
print(countDNA(dna))
print(changeToRNA(dna))