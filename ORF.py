#Open Reading Frames

fasta = """>Rosalind_6124
GTTGTATCCCCCCAACTGTCGGAGAAGGCGTTCGGAGTAAATGGAAATAATACTCATCGC
CCCGATCCCGATCTCGCATTATGCCATACGGCCTCCATAGATGAGTGACCTGGACAACCT
GACGAAGGCAGGTCAGAAATTAATCTCAAAATCGATAAAGACTCGAGTTCGTAGCTACTC
GAGTATCACCTTGGTGACTCGTTTGGACATTCACTTGGAGATGCACTCTCCGTACGAGTC
TCGATATTCATAGAGATGGTATCCGGCGCGTTCGCAGGCGCTTCATATCGAGCAAACAGT
CACATGCTCGATGAGGTGCGACTTTAGGGCGCTCGCGGCGCGTCTTTGACTTAACCCGAT
AACCCGCTGAGATCAATGCAAGACCATGAGCACGACGTACAAATCCAGATGCTCCAGGAA
CGTTGAATAGAGACGACGGACCATGCGGACTGTGACCGATGGTTTTTAGCTAAAAACCAT
CGGTCACAGTCCGCATGGATAGTTAATGGTAATATCTTAGCATATCTTGTGGTCCAGACC
TATGGGAGGCGGCTATACCGGAGGTCGTTGCCTAGTCACCCCGTTCGGAGACAAGCCAAA
AATAATCGGTGGGTAGACTCCGAACGCCTATTACCTGTCCATTGGGCTGTAGAGACCCAC
ATTTTGCGGCAAGTTATTCAGCTGTATGATTTATTTGCGGGCCCTAGGGGATGCCCTGCC
CATCTCCGAAGATGAGTCACAACGCCGCGCGGGGACTACATACTTAAGTTTTAGACTTCG
TGCTCGTATTCGTTGACGGTGAGATCTACAACGGCCCAATGGCTCCCCAGCGTACTACTG
GGTGATACTTCGTACAAACCCTGCACGTACCAGGCTGCCCAAGGCTCTCGCGTGCGTTTG
CAACTTCCACACCGGGGAAGTGTTATATGCCCCAGACA"""

codons = {
"UUU" : "F","CUU" : "L",
"AUU" : "I","GUU" : "V",
"UUC" : "F","CUC" : "L",
"AUC" : "I","GUC" : "V",
"UUA" : "L","CUA" : "L",
"AUA" : "I","GUA" : "V",
"UUG" : "L","CUG" : "L",
"AUG" : "M","GUG" : "V",
"UCU" : "S","CCU" : "P",
"ACU" : "T","GCU" : "A",
"UCC" : "S","CCC" : "P",
"ACC" : "T","GCC" : "A",
"UCA" : "S","CCA" : "P",
"ACA" : "T","GCA" : "A",
"UCG" : "S","CCG" : "P",
"ACG" : "T","GCG" : "A",
"UAU" : "Y","CAU" : "H",
"AAU" : "N","GAU" : "D",
"UAC" : "Y","CAC" : "H",
"AAC" : "N","GAC" : "D",
"UAA" : "Stop","CAA" : "Q",
"AAA" : "K","GAA" : "E",
"UAG" : "Stop","CAG" : "Q",
"AAG" : "K","GAG" : "E",
"UGU" : "C","CGU" : "R",
"AGU" : "S","GGU" : "G",
"UGC" : "C","CGC" : "R",
"AGC" : "S","GGC" : "G",
"UGA" : "Stop","CGA" : "R",
"AGA" : "R","GGA" : "G",
"UGG" : "W","CGG" : "R",
"AGG" : "R","GGG" : "G"
}

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

def find_motiv(sequence, motiv):
    position_list = []
    position = 1
    a = 0
    while position > 0:
        position = sequence.find(motiv, a,)  #if not found, returns -1
        position_list.append(position)       #converted to string to join elements later
        a = position+1                       #next iteration: start search after found pattern
    position_list = position_list[:-1]       #while loop stops AFTER pattern not found -> delete last item
    return position_list

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




fasta_dict = fasta_into_dict(fasta)

protein_list = []

for header, sequence in fasta_dict.items():
    RNA = sequence.replace('T', 'U')
    start_position = find_motiv(RNA, 'AUG')
    for i in start_position:
        protein = []
        for j in range(i,len(RNA), 3):
            triplet = RNA[j:j+3]
            aa = codons.get(triplet)
            if aa == 'Stop':
                protein.append(aa)
                break
            else:
                protein.append(aa)
        if protein[-1] == 'Stop':
            protein = protein[:-1]
            protein_list.append(''.join(protein))

for header, sequence in fasta_dict.items():
    sequence = reverse_complement(sequence)
    RNA = sequence.replace('T', 'U')
    start_position = find_motiv(RNA, 'AUG')
    for i in start_position:
        protein = []
        for j in range(i,len(RNA), 3):
            triplet = RNA[j:j+3]
            aa = codons.get(triplet)
            if aa == 'Stop':
                protein.append(aa)
                break
            else:
                protein.append(aa)
        if protein[-1] == 'Stop':
            protein = protein[:-1]
            protein_list.append(''.join(protein))

unique_protein_list = list(set(protein_list))
for i in unique_protein_list:
    print(i)
