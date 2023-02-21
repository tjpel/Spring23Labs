#Thomas Pelowitz for CS368 on 2/14/23

import re
#PROT
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

def prot2 (s: str) -> str:
    number_of_codons = len(s) // 3

    protein = ""
    for i in range(number_of_codons):
        protein += CODON[s[i*3: (i*3)+3]]

    return protein

#DNA and RNA
def dna(s: str) -> dict:
    """
    
    """
    return {"A": len(re.findall('A', s)), 
            "T": len(re.findall('T', s)), 
            "C": len(re.findall('C', s)), 
            "G": len(re.findall('G', s))}

def rna(s: str) -> str:
    return re.sub('T', 'U', s)

#def checkDNAerror(s: str) -> bool:
