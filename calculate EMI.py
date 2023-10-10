#Assignment-1
#Write a program to calculate emi

p=int(input("Enter principle amount:"))
t=int(input("Enter the time:"))
r=int(input("Enter the rate of interest:"))
si=p*t*r/100
print(si)
emi=si+p/12
print(emi)
