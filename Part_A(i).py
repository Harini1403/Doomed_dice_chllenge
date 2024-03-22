Die_A_count=6
Die_B_count=6
sum=0
for i in range (1,Die_A_count+1):
    for j in range(1,Die_B_count+1):
        sum=sum+1
print("Using the additive principle the number of possible combinations are ",sum)
print("Using multiplicative principle the number of combinations are",Die_A_count*Die_B_count)
