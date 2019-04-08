#Namta
start = int(input("The Starting value:"))
stop = int(input("The last value:"))
odd = 0
even = 0
total = 0

while (start <= stop):
    pass
    for x in range(1,10+1):
        count = start * x
        print(start,"X",x,"=",count)
        if (count % 2 == 0):
            even = even + 1
        elif (count % 2 !=0):
            odd = odd + 1
        total = total + count
    start += 1
print("Even:",even)
print("odd:",odd)
print("sum:",total)
print("Coded By Rihan")