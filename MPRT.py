#Finding a Protein Motif

import urllib.request, urllib.error, urllib.parse

uniprot_id = '''A1JP66
P06765_PLF4_RAT
P01878_ALC_MOUSE
P11171_41_HUMAN
A8F2D7
P28653_PGS1_MOUSE
P23185
P07204_TRBM_HUMAN
P02725_GLP_PIG
Q0TMT1
Q8P5E4
P01233_CGHB_HUMAN
B0RU89
A6WKC3
'''.splitlines()

for id in uniprot_id:
    url = 'http://www.uniprot.org/uniprot/{}.fasta'.format(id)
    response = urllib.request.urlopen(url)
    webContent = response.read()
    fasta_list_encoded = webContent.splitlines()
    del fasta_list_encoded[0]           #removing header
    fasta_list = []
    for i in fasta_list_encoded:
        decoded_line = i.decode('ASCII')
        fasta_list.append(decoded_line)
    fasta = ''.join(fasta_list)     #join elements
    position_list = []
    for i in range(len(fasta)):
        if (fasta[i] == 'N') and (fasta[i+1] != 'P') and (fasta[i+3] != 'P'):
            if fasta[i+2] == 'S' or fasta[i+2] == 'T':
                position_list.append(str(i+1))
    if position_list:
        print(id)
        print(' '.join(position_list))
