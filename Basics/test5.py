# gross salary program

# bsa stands for basic salary
bsa = (int)(input("Enter Basic Salary: "))

if(bsa < 1500):
    hra = (float)(bsa * 0.1)
    da = (float)(bsa * 0.9)
else:
    hra = 500
    da = (float)(bsa * 0.98)

# gs stands for gross salary
gs = bsa + hra + da

print("Gross Salary: Rs.", gs)
