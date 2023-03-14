import sequence_infile as si
import nucleotides as nt

def main():
    filename = input("Please enter a filename of raw sequence data.")
    dna = si.raw(filename)
    print(dna)

    filename = input("Please enter a filename of FASTA data.")
    dna = si.fasta(filename)
    print(dna)

    filename = input("Please enter a filename of GenBank data.")
    dna = si.genbank(filename)
    print(dna)
    print(nt.transcription(dna))
    print(nt.count_bases(dna))

if __name__ == "__main__":
    main()