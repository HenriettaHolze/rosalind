#Mendel's First Law

#k = AA
#m = Aa
#n = aa

k = 26
m = 29
n = 18
sum = k + m + n
p_dom = (k/(sum)) * ((k-1)/(sum-1) + m/(sum-1) + n/(sum-1)) + m/sum * (k/(sum-1) + (m-1)/(sum-1) * 0.75 + n/(sum-1) * 0.5) + n/sum * (k/(sum-1) + m/(sum-1) * 0.5)

print(p_dom)
