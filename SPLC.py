#RNA Splicing


fasta = '''>Rosalind_7561
ATGGCGAGAAATATAACTAAGTCGACTTTTTGCTTGCCCGTTATGCCATGCTGCACACAC
CGCACCACAGCCGAAAAGAGTGGACGAGGGTTCTATTGGGTTTACTCAGGCTACTCGTGG
TAGCGGCTACTAGGACATGTAAACGGGACTTCTACGGGGACGAAACCAGTAGGTTAATTT
ACGTGCGGGTCTCTACCGCGTACTGCGGATACCACATGTTATCGGCGGTCCGTCCGAACC
CGTCTGACTGGCGCTGGTGTTTGTGCGCTCCCAACCTTATGCTTCCCGAACTTAAGAGCC
AGAACAAGCTGTCACATTGCGGCTGCACAGTAGCGGGGAAGGTTTGGCAGCGAGGAACCG
GGCAAACCTTCGCTGCTTCCGCCGTAATCCAGGAGCTAAAGTGACACGCATTTGGACACT
CATGGTTGGGAAGTTTTGTGTTGGTGGAGAGAAAGGATGCTCGGGCGCGTTTACCAGCGG
CTCTGGTGGAGTGATGCTTCTGGTGGTCTCGCATTCGCCATATGGTGATCCATGTCCCAG
AACCGATAGCCTGAAGATAAGGCCCCGCCAGTGGCCGCTTGGATAAAAACCTTTTTAAGT
CGGTTGGAAGGTCTTCTGGATGGTTACCCGACGCATACGGAGGAGTTACGGATTCTTTCT
CATTGGTGCAGGAGACCTACGACTTTGCGTGGGATAGCTCAAGCGGCCCTGGTTTCCCCA
CTTCTTCCGGATTCAGGATATTTCGGACGGGCCCCGGGACTTCTGGGCCCGTTGCGGCGT
AGAGTACTGGTACGACCTTTAAACAGTAGCGTCCGGGCCTGGAGACCAGACACCTTAAAG
GTCAGATGTGAGCTAGCCTGTTAAAACGGATGCAAACTAGCTCAGACAGTCTTCGCGATA
CTTTAA
>Rosalind_2493
GTGGAGTGATGCTTCTGGTGGTCTCGCATTCG
>Rosalind_0534
GCGGCTACTAGGACATGTAAACGGGACTTCTAC
>Rosalind_2653
ACACACCGCACCACAGCCGAAAAGAGTGGACGAGGGTTCTA
>Rosalind_9219
CTTCTGGATGGTTACCCGACGCATACGGAGGAGTTACGGATTCTTTCT
>Rosalind_4985
ACCGGGCAAACCTT
>Rosalind_7681
CAGTGGCCGCTTGGATAAAAACCTTTTTA
>Rosalind_4266
TCTACCGCGTACTGCGGAT
>Rosalind_1792
GTTGCGGCGT
>Rosalind_6172
AACAAGCTGTCACATTGC
>Rosalind_7773
ATTTGGACACTCATGGTTG
>Rosalind_7999
ACCTTAAAGGTCAGATGTGAGCTAGCCTGTTAA
>Rosalind_2178
GGTGTTTGTGC
>Rosalind_4508
GCCCTGGTTTCCCCACTTCT'''

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

def DNA_into_prot(DNA):
    RNA = DNA.replace('T', 'U')
    protein = []
    for i in range(0, len(RNA), 3):
        triplet = RNA[i:i+3]
        aa = codons.get(triplet)
        if aa == 'Stop':
            protein.append(aa)
            break
        else:
            protein.append(aa)
    if protein[-1] == 'Stop':
        protein = protein[:-1]
    protein = ''.join(protein)
    return protein

fasta_dict = fasta_into_dict(fasta)

intron_list = []
for header, sequence in fasta_dict.items():         #loop over sequences in fasta file (here not necessary)
    if header == fasta.split()[0][1:]:              #compare without '>'
        exon = sequence
    else:
        intron_list.append(sequence)

for intron in intron_list:
    exon = exon.replace(intron,'')

print(exon)
protein = DNA_into_prot(exon)
print(protein)
