def Power(x:int,c:int,n:int):
    c = bin(c).replace('0b', '')
    nums = list(c)
    nums.reverse()
    l = len(nums)
    z = 1
    i = l-1
    while i >=0:
        z = (z*z)%n
        if nums[i] == '1':
            z = (z*x)%n
        i -= 1
    return z
