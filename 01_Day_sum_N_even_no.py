n = int(input("Enter the value 'N': "))
sum = 0
i=0
while i <= n:
    if i%2==0:
        sum = sum + i
    i += 1
print(sum)