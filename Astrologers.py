print("Welcome to Astrologer's stars\n")
n=int(input("Enter no. of rows:\n"))
bol=int(input("Enter 0 or 1\n"))
if bol==1:
    for i in range(1,n+1):
            print("*"*i)
elif bol==0:
    for i in range(n,0,-1):
            print("*"*i)
