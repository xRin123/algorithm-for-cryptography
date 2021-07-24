def Jacobi(a:int,n:int):
    if a == 0:
        return(0)
    else:
        #预先设定ans
        ans = 1
        while a!= 1 and a!=2:
            a = a%n
            #判断n模8的值
            if n%8 == 1 or n%8 == 7:
                t = 1
            else:
                t = -1
            #约化a中所有的2
            while a%2 == 0 :
                a = a/2
                ans = t*ans
            #最后a没法继续约化时，交换an的值
            if n%4 == 3 and a%4 == 3:
                ans = -ans
            else:
                ans = ans
            if a!=1:
                x = a
                a = n
                n = x
        #循环结束后a为1
        ans = ans+0
        return(ans)












