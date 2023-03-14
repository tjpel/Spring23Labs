CODON = {
    "UUU": "F",
    "UUC": "F",
    "CUU": "L",
    "CUC": "L",
    "AUU": "I",
    "AUC": "I",
    "GUU": "V",
    "GUC": "V"
}

def transcription(s: str) -> str:
    """
    Transcribes DNA to RNA
    """
    return s.replace("T", "U")

def count_bases(s: str) -> tuple:
    """
    Counts the number of each type of base (nucleotide) in a DNA sequence.
    """
    return (s.count("A"), s.count("T"), s.count("C"), s.count("G"))

def prot(s: str) -> str:
    """
    Translates an RNA sequence into protein (single-letter notation).
    """

    current = ""
    output = ""

    for char in s:
        current += char

        if len(current) == 3:
            output += CODON[current]
            current = ""

    return output