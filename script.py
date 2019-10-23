#Rabbits and Recurrence Relations

rabbits = 1
adult_rabbits = 0
for i in range(1,n+1):
    adult_rabbits += baby_rabbits
    baby_rabbits = adult_rabbits * k
    rabbits += baby_rabbits
    i += 1

n = 5
k = 3

i = 1
baby_rabbits = 1
adult_rabbits = 0
adult_rabbits_new = 0
for i in range(1,n):
    adult_rabbits_new += baby_rabbits
    baby_rabbits = adult_rabbits * k
    rabbits = adult_rabbits + baby_rabbits
    adult_rabbits = adult_rabbits_new
    i += 1

print(rabbits)

baby_rabbits = 0
adult_rabbits = 1
rabbits = 1
if i == 1:
    print(rabbits)
elif i == 2:
    print(rabbits)
else:
    for i in range(2,n):
        adult_rabbits += baby_rabbits
        baby_rabbits +=


#items in dict -> required number of appearence
fasta = """>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA"""

fasta_dict = fasta_into_dict(fasta)

sequence_list = []
for header, sequence in fasta_dict.items():
    sequence_list.append(sequence)

first_seq = sequence_list[0]


for i in range(len(first_seq)):
    for j in sequence_list:
        if sequence[a:+b] in i:
            break
