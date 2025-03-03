#Complementing a Strand of DNA
DNA = "GGCTCGCGAGCGAAGCAGCGAGATTACCGGGGAGGCCACCCTAGTTTTTAAGAACTCACAGATATTCAGTACAAGACAATAATCCTAGTAAACACATGGCTTAACCTGTACTTGCGCTCGAAACCACCTCTTGGCTGATGAGTCGCACTCAGTACCTTCGTTGCCCCCCTAGTCTTAGTATAGGACGAAGGAGCTAGCCATGCCTTGTAAAGTGCTTTCAGTCCCCCCCTCACAAGATCCTTGGTCGGAGTGTCCACGACCAGTGTATGCTAAGCGCTTCCCGGATTCGTCGTAAATAATCATCGGCGATAAACAAAACTCGAAGATGTGTTCGACTTATTCTCCGGCCGATGGATAGATTGAGAACTCGTGGGTGGCTGCGTCTGGAGCCTCTACGACGACTAACGGTGGCTTCAGAACAAACTACTCCGCACCAAGTCACCTCTCGCTAGGGGAGAGTTGCTGAGTCACCAGGGGAATAACTTATTCTATTGAATTTCCAACACGATCTGTTTGATGAGCCTAACAGAGGCCACGGGCGGGGGCTCGCGTTGGGCCCAACCTCAGAACTGGTCCATTCGTTCCCTCGGTGCTACAACCACTGCGGACACTCTGCCAGACTAAAGCTTTGTCGTGTGTCTCCTTCCATGGGCAATCCATCTCATATCCGCATACATAGGGCTCTGACACGCCATAGCCTCAAACTAAAGCGCAGGGACAAGCTTAAATATACAGGGTCCATACTGCATCCTCCAAGTGACGTGACGTAGCCCATCCCCAAAATAAATAGATGCCGCGAACGGTCAACTCCTAACCACAGCGCTAGACTTGTGGATGGAGTGCCCTGTACGTGCGCGGGGGCCCCTAATAGGATATGTCGCACC"

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
print(reverse_complement)
