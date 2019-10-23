#Locating Restriction Sites
#position and length of reverse palindrome

fasta = """>Rosalind_9452
ATATCAACTGTGGGCAAGATACTTCAAGCGTTTGATACAGTTGCCTCCGCCTTAGGCGCA
TACATCCAACAAAGGCCGCGCGTGGCCAATGAGGAATGAGGAGTTCCAGGCTAGAACAAA
CTTGACTAGGTGCTGACTATAGGCCTTGCCCGACACGGAACAGGGACCTCATTTACTGGA
TGCCTCCGATGCTCCGAATCGTGAAAGTCTGATAGACCAACATATTAATCGAACGAGGGG
ACAGGTCTTCTCAAACTCTCTGCCTTAGAGGCCCCTTATAGCTAGGTATCTGGGATGAAG
CGTATTACGAACCCGCAAATGTCATGATACTGAACCGTGGGACTGCAGATCCTGAGTGCC
CTCCCAGAACCCATCCTTTACATACTCAGCCTTTATAGTTAGAGTTCTCGGGTCGCTGGC
GTGTGGCCAAACCTAGAAGAAATCCAAAAGTGTCCGAATTCGGACCTGCTAGAACGCCAG
TAACGGATGGCGAAACACCAGCCACTGTACATCGGGGGCATTCCCTTTCTTGTGCCCTTC
CGTGAAAACGTTAGAACGGTTCTCCTAATATGGATTCGTTGAGGCTTCCGGCTCCTGAAT
TAGGGTTATTGAAAATATTGTGTATCGACACATTATAACATTAAAAGGTGCTAGAAAACG
ATATGAGTTTCAATCCCGGCGCGCTATGACTCTGTCGGACTCCTCACGGTTAGTTGCTTT
CATGTTAAATATTCAGCAGATAAATACGGTATCGGCAAGCCAGCTTATGCACGGCTCTTC
CCGACTTGAACACAGGAGAACCGCAACCAGGGTCTTAGCCGAGGACCATATTCTTCATTG
CCACAACGGGGCCTAACCGCCACAAGTCTCAATCAGACATTAGACCCGGGATTGGGATCG
GCCGATTCCGGGGCGC"""

def reverse_complement(dna):
    DNA = dna.upper()
    DNA_list = list(DNA)
    complement_list = []
    for i in DNA_list:
        if i == 'A':
            complement_list.append('T')
        elif i == 'T':
            complement_list.append('A')
        elif i == 'G':
            complement_list.append('C')
        elif i == 'C':
            complement_list.append('G')
    reverse_complement_list = complement_list
    reverse_complement_list.reverse()
    s = ''
    reverse_complement = s.join(reverse_complement_list)
    return reverse_complement

def fasta_into_dict(fasta):
    fasta_list = fasta.split()
    fasta_dict = {}
    for line in fasta_list:
        if line[0] == '>':
            header = line[1:]
            fasta_dict[header] = []
        else:
            fasta_dict[header].append(line[:])  #creates list within value {'header': ['ABS', 'ABC']}
    for header in fasta_dict:
        fasta_dict[header] = ''.join(fasta_dict[header])
    return fasta_dict

fasta_dict = fasta_into_dict(fasta)

for header, sequence in fasta_dict.items():         #loop over sequences in fasta file (here not necessary)
    for i in range(len(sequence)):                  #iterate over every base in sequence
        for a in range(2, 7):                       #reverse palindrome of length 4-12
            first = sequence[i : i + a]             #first half of palindrome
            second = sequence[i + a : i + a * 2]    #second half
            reversec = reverse_complement(second)   #reverse complement of second half
            if first == reversec:                   #check if identical
                print(i+1, a*2)                     #print position and length
