#Thomas Pelowitz, 03/14/23

import re

def raw(infile: str) -> str:
    try:
        with open(infile, 'r') as f:
            dna = f.read()
        dna = re.sub(r'\n', '', dna)
        return dna.upper()
    except FileNotFoundError:
            print("File not found.")
            return ''
        
def fasta(infile: str) -> str:
    try:
        with open(infile, 'r') as f:
            f.readline()
            dna = f.read()
        dna = re.sub(r'\n', '', dna)
        return dna.upper()
    except FileNotFoundError:
            print("File not found.")
            return ''

def genbank(infile: str) -> str:
    try:
        with open(infile, 'r') as f:
            dna = f.read()
        dna = re.sub(r'[\n\s\d]', '', dna)
        return dna.upper()
    except FileNotFoundError:
            print("File not found.")
            return ''


def main():
    filename = input("Please enter a filename of raw sequence data.")
    dna = raw(filename)
    print(dna)

    filename = input("Please enter a filename of FASTA data.")
    dna = fasta(filename)
    print(dna)

    filename = input("Please enter a filename of GenBank data.")
    dna = genbank(filename)
    print(dna)

if __name__ == "__main__":
    main()