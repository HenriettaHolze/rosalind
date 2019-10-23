#Finding a Motif in DNA

s = "ACCGGTAGATACCGGTAGGCCCGGTAGTTCCGGTAGCCGGTAGGGTCCGGTAGGACCGGTAGCCGGTAGGCCGGTAGCCGGTAGGACCGGTAGCCGGTAGCTCCCGGTAGTCCGGTAGTCCGGTAGCTAAATCGGCCCGGTAGAACCGGTAGGCCCGGTAGGTACCGGTAGCCGGTAGCTCCGGTAGCCCGGTAGGCCGGTAGGTATAATGCCGGTAGCCGCCGGTAGAACCGGTAGCCGGTAGACCGGTAGTATTCGCCGGTAGAGGTAGTGACCACGCCACCGGTAGCCGGTAGCCGGTAGTCCGCCCGGTAGATCCGGTAGCCGGTAGCCACCGTAGGCCCCCGGTAGTCCGGTAGGGCCGGTAGGCTAACCGGTAGACCCGGTAGGCCCGGTAGGCCGGTAGCCCCGGTAGTCCGGTAGCCGGTAGGCCGGTAGTCCGGTAGACCGGTAGTGTACCGGTAGTCCACCGGTAGCCGGTAGCCGGTAGGGACCGGTAGCCGGTAGACGTTTGGCAGTGTCCGGTAGCCCGGTAGCCCGGTAGTCCCCGGTAGCACCGGTAGAGACCGGTAGACCCACCGGTAGCTACCGGTAGGTGAGCCGGTAGATTCCCGGTAGGCCGGTAGACCGGTAGGGGAAGTAACGGGCCGGTAGCCGGTAGGCCGGTAGGCCGGTAGCCGGTAGGGCCGGTAGCCGGTAGCCGGTAGCCCGGTAGCCGGTAGGGAATTCCGGTAGCCGGTAGAGCCGGTAGGTGCCCGGTAGCCGGTAGCCCCCTCCGGTAGTCCGGTAGTTATCCCGGTAGTCGGCCGGTAGTACCGGTAGCCGGTAGTCGGCCGGTAGGCCGGTAGATTGGTTGCCGGTAGGCCGGTAGTCCGGTAGACTCGCCGGTAGCCGGTAGGAGACCCGGTAGCCGGTAG"
t = "CCGGTAGCC"

position_list = []
position = 1
a = 0
while position > 0:
    position = s.find(t, a,)                    #if not found, returns -1
    position_list.append(str(position+1))       #converted to string to join elements later
    a = position+1                              #next iteration: start search after found pattern

del position_list[-1]                           #while loop stops AFTER pattern not found -> delete last item
' '.join(position_list)                         #only delimited by space
