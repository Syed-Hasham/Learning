def sumofn(n):
    if n == 0:
        return 0
    elif n==1: 
        return 1
    else:
        return sumofn(n-1)+n
    
print(sumofn(4))