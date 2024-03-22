Die_A_count=6
Die_B_count=6
s=0
total_outcomes=Die_A_count*Die_B_count
sum=[2,3,4,5,6,7,8,9,10,11,12]
probability=[0,0,0,0,0,0,0,0,0,0,0]
for i in range (1,Die_A_count+1):
    for j in range(1,Die_B_count+1):
        s=i+j
        if s in sum:
            probability[s-2]+=1   
print("Count of sums:",probability)
for i in range (len(probability)):
    print("P(Sum={}) = {:.2f}".format(sum[i], probability[i] / total_outcomes))
