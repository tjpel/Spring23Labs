#Thomas Pelowitz for CS368 on 2/14/23
import nucleotides as nt
import re

def main():
    print(nt.prot("AUU"))

    while True:
        seq = input("Please enter a DNA sequence.   ")
        m = re.search('[^ACGT]', seq)
        if m == None:
            break
        

    print(nt.dna(seq))
    print(nt.rna(seq))


if __name__ == "__main__":
    main()