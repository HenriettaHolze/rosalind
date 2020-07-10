#Calculating Expected Offspring
numbers = "17013 16152 17290 18969 19557 16009"

a, b, c, d, e, f = [int(i) for i in numbers.split()]

sum = a + b + c + d + e + f

dom_offspr = (a + b + c + d * 0.75 + e * 0.5) * 2
print(dom_offspr)
rec_offspr = (f + e * 0.5 + d * 0.25) * 2
#print(rec_offspr)
print(sum*2 == dom_offspr + rec_offspr)
