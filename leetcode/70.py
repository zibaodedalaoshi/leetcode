def climbStairs(n: int) -> int:
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        a=1
        b=2
        temp=0
        for i in range(3,n+1):
            temp = a+b
            a=b
            b=temp
        return temp


print(climbStairs(30))

#通过，时间击败99.25%，空间击败42.37%