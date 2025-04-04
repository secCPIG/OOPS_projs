def getSum():
    l=int(input())
    for i in range(l):
        n=int(input())
        sum = 0
        for digit in str(n):  
            sum += int(digit)       
        print(sum)
getSum()