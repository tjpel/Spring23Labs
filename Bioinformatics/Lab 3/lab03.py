#Thomas Pelowitz for CS368 on 2/14/23

#PROT
codon = {
    "UUU": "F",
    "UUC": "F",
    "CUU": "L",
    "CUC": "L",
    "AUU": "I",
    "AUC": "I",
    "GUU": "V",
    "GUC": "V"
}

def prot(s: str) -> str:
    """
    Translates an RNA sequence into protein (single-letter notation).
    """

    current = ""
    output = ""

    for char in s:
        current += char

        if len(current) == 3:
            output += codon[current]
            current = ""

    return output

print(prot("AUCGUU"))

